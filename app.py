import pandas as pd
from dash import Dash, html, dcc, Input, Output
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

app.layout = html.Div(

    style={
        "backgroundColor": "#f4f6f9",
        "padding": "20px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Analysis",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Hr(),

        html.Label(
            "Select Region",
            style={
                "fontSize": "20px",
                "fontWeight": "bold"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-chart")
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)"
        }
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)