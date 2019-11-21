# sample code for reading data from different sources

# read json data into pandas dataframe
import pandas as pd
import urllib.request
import json

with urllib.request.urlopen(url) as file:
    a = json.loads(file.read())
    df = pd.DataFrame.from_dict(a)
    
