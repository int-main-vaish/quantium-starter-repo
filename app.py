import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Group sales by date
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels=
    {
        "Date": "Date",
        "Sales": "Total Sales ($)"
    }

)
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    annotation_text="Price Increase",
    annotation_position="top right"
)
fig.update_layout(
    width=1000,
    height=600
)
fig.update_xaxes(
    tickformat="%Y-%m",
    tickangle=45
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)