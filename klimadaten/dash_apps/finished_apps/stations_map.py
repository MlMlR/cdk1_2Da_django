from dash import dcc, html
from datetime import date
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from klimadaten.models import City, Weather
import plotly.express as px
import pandas as pd

EUROPE_NORTH = 71.5  # North Cape in Norway
EUROPE_SOUTH = 36  # Punta de Tarifa in Spain
EUROPE_WEST = -25  # Iceland
EUROPE_EAST = 60  # Ural Mountains in Russia

# Create a Dash app for displaying stations on a map
sapp = DjangoDash('StationsMap')

sapp.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker',
        date='1979-12-05',  # Default date
    ),
    dcc.Graph(id='city-map'),
])


@sapp.callback(
    Output('city-map', 'figure'),
    [Input('date-picker', 'value')]
)
def update_map(date):
    df = fetch_data(date)
    # fig = px.scatter_mapbox(
    fig = px.scatter_geo(
        df,
        lat="city__lat",
        lon="city__lon",
        hover_name="city__name",
        hover_data=["max_windspeed"],
        color="max_windspeed",
        color_continuous_scale=px.colors.sequential.Turbo,
        # zoom=6,
        # mapbox_style="open-street-map"
        # height=300,
    )
    fig.update_layout(coloraxis_colorbar_title_text='Max Wind Speed (km/h)')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(
        mapbox_bounds={"west": EUROPE_WEST,
                       "east": EUROPE_EAST,
                       "south": EUROPE_SOUTH,
                       "north": EUROPE_NORTH})
    return fig


def fetch_data(selected_date: date):
    # Fetch Weather records for the given date with related City data pre-joined
    weather_records = Weather.objects.select_related('city')

    # Construct a DataFrame from the queryset
    data = weather_records.values(
        'city__name',  # Accesses the `name` field from the related City model
        'city__country',  # Accesses the `country` field from the related City model
        'city__lat',  # Accesses the `lat` field from the related City model
        'city__lon',  # Accesses the `lon` field from the related City model
        'max_windspeed',  # Field from the Weather model
    )

    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    ...