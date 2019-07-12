import pandas as pd
import numpy as np
import json
from sklearn.neighbors import NearestNeighbors

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# create dataframe where features are converted to a list
allfruits_df = pd.read_csv('static/fruits_sample.csv')
selection_df = allfruits_df.copy()
selection_df['features'] = selection_df.values[:,3:].tolist()
selection_df = selection_df[['fruit_number','filename','fruit','features']]

# set up KNNs using KD-tree algorithm
X = np.array(selection_df['features'].values.tolist())
nbrs = NearestNeighbors(n_neighbors=18, algorithm='kd_tree').fit(X)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/favfinder")
def fav():
    """Fruit and veggie finder page."""
    return render_template("favfinder.html")

@app.route("/relatedFavfinder")
def relatedFavfinder():
    """Fruit and veggie finder page."""
    return render_template("relatedfavfinder.html")

@app.route("/fruit_choice/<choice>")
def fruit_choice(choice):

    # calculate 18 k-nearest neighors based on user 'choice'
    distances, indices = nbrs.kneighbors([X[int(choice)]])
    idx = list(np.ndarray.flatten(indices))
    fruitchoice_df = selection_df.iloc[idx,:]
    fruitchoice_df = fruitchoice_df.assign(distance = distances.tolist()[0])

    # output to json
    output_df = fruitchoice_df[['fruit_number','fruit', 'filename', 'distance']]
    fruit_data = output_df.to_dict('records')
    return jsonify(fruit_data)

@app.route("/allFruits")
def allFruits():

    # create dataframe where features are converted to a list
    #selection_df = pd.read_csv('static/fruits_sample.csv')
    
    # output to json
    output_df = allfruits_df[['fruit_number','fruit', 'filename']]
    fruit_data = output_df.to_dict('records')
    return jsonify(fruit_data)

if __name__ == "__main__":
    app.run()