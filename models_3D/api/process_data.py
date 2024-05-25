import pandas as pd
import json

json_file = "response.json"

with open(json_file, 'r') as j:
    json_dict = json.load(j)

items  = json_dict['data']['morePrints']['items']
# print(len(items))

df = pd.DataFrame(items)
print(df.columns)