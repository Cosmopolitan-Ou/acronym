# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:26:01 2022

@author: knmc887
"""

from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np


# utility functions
###############################################################################

# function to read excel file for multiple sheets into one dataframe
def read_xl(file):
    out = pd.DataFrame()
    xls = pd.ExcelFile(file)
    for sheet in xls.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        out = pd.concat([out, df])
    return out

# function to turn dataframe into dictionary
def get_dict(dataframe):
    keys = pd.unique(dataframe[0])
    f = lambda x: dataframe[dataframe[0] == x][1].values
    vfunc = np.vectorize(f)
    df_map = pd.DataFrame({"key": keys, "value": vfunc(keys)})
    out = dict(zip(df_map["key"].str.strip().str.upper(), df_map["value"]))
    return out

# function to get dinctionary value(s) by key
def get_value(key, dictionary):
    key = key.strip().upper()
    value = dictionary.get(key)
    if value is None: return ["-Not Found-"]
    if value.size == 1: 
        return value.tolist()
    else:
        return([str(i + 1) + ". " + item + " " for i, item in enumerate(value)])

# function to insert item in between elements within a list
def intersperse(lst, item):
    out = [item] * (2*len(lst) - 1)
    out[0::2] = lst
    return out
###############################################################################


# global paramters
MAPPING_FILE = "Acronym dictionary.xlsx"
TITLE = "Acronym Dictionary Search Tool"

# get dictionary
d = get_dict(read_xl(MAPPING_FILE))


# Dash Part
###############################################################################

# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

#initiation
app = Dash(__name__, 
           title = TITLE, 
           update_title = "Loading...",
           external_scripts=external_scripts,
           external_stylesheets=external_stylesheets)

# UI
app.layout = html.Div(children=[
    html.H1(TITLE),
    dbc.Input(id="input",
              placeholder="Type a word to search (Case insensitive)..."),
    html.Br(),
    html.H3("Explanation:"),
    html.Div(id="output")
    ])

# callbacks
@app.callback(
    Output("output", "children"),
    [Input("input", "value")]
    )
def show_rel(val):
    if val is None or len(val) == 0: 
        return "-No Input-"
    else:
        return intersperse(get_value(val, d), html.Br())

# run app
if __name__ == "__main__":
    app.run_server(debug=True)
###############################################################################

        
    