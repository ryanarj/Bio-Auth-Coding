import numpy as np
from scipy.spatial import distance
import pandas as pd


def euclidean_distance(x, y):
    return distance.euclidean(x, y)

def compute_intrasimilarity(data, n, col):
    # https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.iloc.html
    intraperson_similarity = 0.0
    chunksize = int(len(data.index) / float(n))
    count = 0.0
        
    for i in range(0, len(data.index)-chunksize, chunksize):        
        for j in range(0, len(data.index)-chunksize, chunksize):
            if i != j:
                intraperson_similarity += euclidean_distance(data.iloc[i:i+chunksize, col], data.iloc[j:j+chunksize, col])
                count += 1.0
            
    return intraperson_similarity / count


np.random.seed(1)
features = pd.read_csv('hw6_data.csv')
features = pd.get_dummies(features, columns=['top-morning-app','top-morning-wifi','day-of-week'])
chunks = 5
intrasim = np.zeros(len(features.columns))

for col in range(len(features.columns)):
   intrasim[col] = compute_intrasimilarity(features, chunks, col)

mean_sim = np.mean(intrasim)
final_features = features.iloc[:, intrasim <= mean_sim]


