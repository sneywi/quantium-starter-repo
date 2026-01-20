import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("processed_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    labels={
        "date": "Date",
        "sales": "Sales ($)",
        "region": "Region"
    }
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Dash Visualiser",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
