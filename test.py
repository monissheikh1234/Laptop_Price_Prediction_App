import pickle

df = pickle.load(open('df.pkl', 'rb'))
print(df.columns)
