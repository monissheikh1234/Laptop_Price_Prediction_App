import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Theme toggle
theme = st.radio("🎨 Choose Theme", ["🌌 Sky Blue", "🌿 Light Green"], horizontal=True)

# Darker custom theme colors
if theme == "🌌 Sky Blue":
    bg_color = "#69BBFF"  # dark sky blue
    text_color = "#331414"
elif theme == "🌿 Light Green":
    bg_color = "#52FFD9"  # dark light green
    text_color = "#331414"

# Inject CSS styles
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    .title-style {{
        text-align: center;
        font-size: 40px;
        color: {text_color};
        font-weight: 800;
        margin-bottom: 20px;
    }}
    .stRadio > div {{
        color: {text_color} !important;
        font-weight: bold;
        font-size: 18px;
    }}
    .stSelectbox label, .stSlider label, .stNumberInput label {{
        font-weight: bold;
        color: {text_color};
        font-size: 16px;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title-style">💻 Laptop Price Predictor</div>', unsafe_allow_html=True)

# ---- Form UI ----
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Brand', df['Company'].unique())
with col2:
    type_name = st.selectbox('Laptop Type', df['Type'].unique())

with col1:
    ram = st.selectbox('RAM (GB)', sorted(df['RAM'].unique()))
with col2:
    weight = st.number_input('Weight (kg)', step=0.1, format="%.2f")

with col1:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
with col2:
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

with col1:
    screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 15.6)
with col2:
    resolution = st.selectbox('Resolution', ['1920x1080', '1366x768', '1600x900',
                                             '3840x2160', '3200x1800', '2880x1800',
                                             '2560x1600', '2560x1440', '2304x1440'])

with col1:
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
with col2:
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

with col1:
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048])
with col2:
    ssd = st.selectbox('SSD (GB)', [0, 128, 256, 512, 1024])

os = st.selectbox('Operating System', df['os'].unique())

# ---- Prediction Logic ----
if st.button("💰 Predict Laptop Price"):
    # Convert text to numeric
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size

    # Build query
    query_df = pd.DataFrame([[
        company, type_name, ram, weight,
        touchscreen_val, ips_val, ppi,
        cpu, hdd, ssd, gpu, os
    ]], columns=['Company', 'Type', 'RAM', 'Weight', 'Touchscreen', 'IPS',
                 'PPI', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

    # Predict
    predicted_price = int(np.exp(pipe.predict(query_df)[0]))

    st.success(f"🎯 Predicted Price: ₹ {predicted_price}")
