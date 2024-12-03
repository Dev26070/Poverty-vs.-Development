import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the dataset
data = pd.read_csv('poverty_development_data.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Poverty vs. Development Dashboard"),
    
    dcc.Graph(
        id='poverty-vs-gdp',
        figure=px.scatter(data, x='GDP_Per_Capita', y='Poverty_Rate',
                          title='Poverty Rate vs GDP Per Capita',
                          labels={'GDP_Per_Capita': 'GDP Per Capita (USD)', 'Poverty_Rate': 'Poverty Rate (%)'},
                          hover_name='Country')
    ),
    
    dcc.Graph(
        id='poverty-vs-hdi',
        figure=px.scatter(data, x='Human_Development_Index', y='Poverty_Rate',
                          title='Poverty Rate vs Human Development Index',
                          labels={'Human_Development_Index': 'Human Development Index', 'Poverty_Rate': 'Poverty Rate (%)'},
                          hover_name='Country')
    ),
    
    dcc.Graph(
        id='poverty-vs-life-expectancy',
        figure=px.scatter(data, x='Life_Expectancy', y='Poverty_Rate',
                          title='Poverty Rate vs Life Expectancy',
                          labels={'Life_Expectancy': 'Life Expectancy (years)', 'Poverty_Rate': 'Poverty Rate (%)'},
                          hover_name='Country')
    ),
    
    dcc.Graph(
        id='gdp-vs-hdi',
        figure=px.scatter(data, x='GDP_Per_Capita', y='Human_Development_Index',
                          title='GDP Per Capita vs Human Development Index',
                          labels={'GDP_Per_Capita': 'GDP Per Capita (USD)', 'Human_Development_Index': 'Human Development Index'},
                          hover_name='Country')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)