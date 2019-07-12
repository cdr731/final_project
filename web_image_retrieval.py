#!/usr/bin/env python
# coding: utf-8

# dependencies
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# selection can be from 0 to 544
choice = int(input('Input choice from 0 to 544: '))

# create dataframe where features are converted to a list
selection_df = pd.read_csv('static/fruits_sample.csv')
selection_df['features'] = selection_df.values[:,2:].tolist()
selection_df = selection_df[['fruit_number','filename','fruit','features']]

# calculate 40 k-nearest neighors based on user 'choice'
X = np.array(selection_df['features'].values.tolist())
nbrs = NearestNeighbors(n_neighbors=40, algorithm='kd_tree').fit(X)
distances, indices = nbrs.kneighbors([X[choice]])
idx = list(np.ndarray.flatten(indices))
selection_df = selection_df.iloc[idx,:]
selection_df = selection_df.assign(distance = distances.tolist()[0])

# output to json
output_df = selection_df[['fruit_number','fruit', 'filename', 'distance']]
json_output = output_df.to_json(orient='records')
print(json_output)