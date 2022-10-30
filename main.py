import pandas as pd
import json

f = open('dataset.json')
valueData = json.load(f)


df = pd.DataFrame(valueData)
df = df.dropna()
df = pd.crosstab(index=df['indicator'],columns=df['year'],values=df['value'],aggfunc='mean')

# Generate html view
out_file = open("./output.html",'w')
out_file.write(df.to_html())
out_file.close()