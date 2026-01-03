import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Create app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Read the wildfire data
df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv'
)

# Extract Month and Year
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
df['Year'] = pd.to_datetime(df['Date']).dt.year

# =========================
# Layout
# =========================
app.layout = html.Div(children=[

    # TASK 2.1: Title
    html.H1(
        'Australia Wildfire Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 26}
    ),

    # Outer division
    html.Div([

        # TASK 2.2: Radio items + dropdown
        html.Div([

            html.H2('Select Region:', style={'margin-right': '2em'}),

            dcc.RadioItems(
                [
                    {"label": "New South Wales", "value": "NSW"},
                    {"label": "Northern Territory", "value": "NT"},
                    {"label": "Queensland", "value": "QL"},
                    {"label": "South Australia", "value": "SA"},
                    {"label": "Tasmania", "value": "TA"},
                    {"label": "Victoria", "value": "VI"},
                    {"label": "Western Australia", "value": "WA"}
                ],
                value='NSW',
                id='region',
                inline=True
            ),

            html.Div([
                html.H2('Select Year:', style={'margin-right': '2em'}),
                dcc.Dropdown(
                    df['Year'].unique(),
                    value=2005,
                    id='year'
                )
            ])
        ]),

        # TASK 2.3: Output divisions
        html.Div([
            html.Div([], id='plot1'),
            html.Div([], id='plot2')
        ])
    ])
])

# =========================
# TASK 2.4 & 2.5: Callback
# =========================
@app.callback(
    [
        Output('plot1', 'children'),
        Output('plot2', 'children')
    ],
    [
        Input('region', 'value'),
        Input('year', 'value')
    ]
)
def reg_year_display(input_region, input_year):

    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Plot 1: Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()

    fig1 = px.pie(
        est_data,
        values='Estimated_fire_area',
        names='Month',
        title="{} : Monthly Average Estimated Fire Area in year {}".format(
            input_region, input_year
        )
    )

    # Plot 2: Monthly Average Count
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()

    fig2 = px.bar(
        veg_data,
        x='Month',
        y='Count',
        title='{} : Average Count of Pixels for Presumed Vegetation Fires in year {}'.format(
            input_region, input_year
        )
    )

    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]


# Run the app
if __name__ == '__main__':
    app.run()