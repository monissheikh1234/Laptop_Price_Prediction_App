import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('laptop_data.csv')

# Clean column names
df.rename(columns={
    'TypeName': 'Type',
    'Inches': 'ScreenSize',
    'ScreenResolution': 'Resolution',
    'Cpu': 'CPU',
    'Ram': 'RAM',
    'Memory': 'Memory',
    'Gpu': 'GPU',
    'OpSys': 'OS'
}, inplace=True)

# Clean RAM column
df['RAM'] = df['RAM'].str.replace('GB', '').astype(int)

# Convert Weight column to float
df['Weight'] = df['Weight'].str.replace('kg', '').astype(float)

# Add Touchscreen and IPS columns
df['Touchscreen'] = df['Resolution'].apply(lambda x: 1 if 'Touchscreen' in x else 0)
df['IPS'] = df['Resolution'].apply(lambda x: 1 if 'IPS' in x else 0)

# Extract resolution and compute PPI
def calculate_ppi(row):
    try:
        res = row['Resolution'].split()[-1]
        x_res, y_res = map(int, res.split('x'))
        return ((x_res**2 + y_res**2)**0.5) / row['ScreenSize']
    except:
        return 0

df['PPI'] = df.apply(calculate_ppi, axis=1)

# Fix Memory parsing and create HDD, SSD columns
df['HDD'] = 0
df['SSD'] = 0

import re
for i in df.index:
    row = df.loc[i, 'Memory']
    row = row.replace('GB', '').replace('TB', '000')

    hdd = ssd = 0
    parts = row.split('+')
    for part in parts:
        part = part.strip()
        size_match = re.match(r'([\d\.]+)', part)
        if size_match:
            size = float(size_match.group(1))
            if 'SSD' in part:
                ssd += int(size)
            else:
                hdd += int(size)

    df.at[i, 'HDD'] = hdd
    df.at[i, 'SSD'] = ssd

# Extract CPU brand
df['Cpu brand'] = df['CPU'].apply(lambda x: x.split()[0])

# Extract GPU brand
df['Gpu brand'] = df['GPU'].apply(lambda x: x.split()[0])

# Clean OS names
df['os'] = df['OS'].apply(lambda x: x if x in ['Windows', 'Mac', 'Linux'] else 'Other')

# Drop unused columns
df = df.drop(columns=['Unnamed: 0', 'ScreenSize', 'Resolution', 'Memory', 'CPU', 'GPU', 'OS'])

# Log-transform target variable
df['Price'] = np.log(df['Price'])
df.rename(columns={
    'TypeName': 'Type',
}, inplace=True)

# Split features and labels
X = df.drop(columns=['Price'])
y = df['Price']

# Define categorical and numerical columns
categorical_cols = ['Company', 'Type', 'Cpu brand', 'Gpu brand', 'os']
numerical_cols = ['RAM', 'Weight', 'Touchscreen', 'IPS', 'PPI', 'HDD', 'SSD']

# Preprocessing pipeline
column_trans = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
], remainder='passthrough')

# Complete pipeline with model
pipe = Pipeline([
    ('transformer', column_trans),
    ('estimator', LinearRegression())
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipe.fit(X_train, y_train)

# Save model and dataframe
pickle.dump(pipe, open('pipe.pkl', 'wb'))
pickle.dump(df, open('df.pkl', 'wb'))

print("Model and data saved successfully.")
