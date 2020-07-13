
import pandas as pd
import requests

response = pd.read_json('output.json',orient='index')
data = pd.DataFrame(response).T
print(data.head())