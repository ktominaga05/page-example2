from pathlib import Path
import plotly.express as px
import os

os.makedirs('output', exist_ok=True)
df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.write_html('output/index.html')
