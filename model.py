import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_csv('stock_data.csv')

features = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
pca.fit(X_scaled)

with open("model.pkl", "wb") as f:
    pickle.dump((pca, scaler), f)
