import pandas as pd
import numpy as np
import plotly.express as px

# Dash imports (used later)
from dash import Dash, dcc, html

df = pd.read_csv("AmesHousing.csv")
print(df.head())

print(df.shape)
df.info()

df.describe()

print(np.mean(df['SalePrice']))
print(np.median(df['SalePrice']))
print(np.std(df['SalePrice']))

print("\n")

print(df.isna().sum()[df.isna().sum() > 0])

df['LotFrontage_normalized'] = (df['Lot Frontage'] - df['Lot Frontage'].mean()) / df['Lot Frontage'].std()

print("\n")

print(df['LotFrontage_normalized'])

print("\n")

fig = px.histogram(df, x='SalePrice', title='Distribution of SalePrice')
fig.show()

#fig = px.histogram(df, x="Gr Liv Area", y="SalePrice", title="Living Area vs Sale Price",)
#fig.show()

#fig = px.box(df, x="Neighborhood", y="SalePrice", title="Sale Price Distribution by Neighborhood")
#fig.show()

app = Dash(__name__)
app.title = "Ames Housing Dashboard"

app.layout = html.Div([

    html.H1("My First Dash App"),
    html.P("This chart shows the distribution of the number of houses bought per price."),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
