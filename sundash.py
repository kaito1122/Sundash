import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
from skimage import io

# default
df_m = pd.read_csv('data/SN_m_tot_V2.0.csv', header=None)
df_m.columns = ['Year', 'Month', 'DecYear', 'Gn', 'StE', 'NumObs', 'Null']

# df_d = pd.read_csv('data/SN_d_tot_V2.0.csv', sep=';')
# df_y = pd.read_csv('data/SN_y_tot_V2.0.csv', sep=';')
# df_ms = pd.read_csv('data/SN_ms_tot_V2.0.csv', sep=';')

app = Dash(__name__)
app.layout = html.Div([
    # Question 1
    html.H4('Interactive Sunspot Graphing'),
    dcc.Graph(id="graph"),
    html.P('Select smoothness:'),
    dcc.Slider(id="smoother", min=1, max=12, step=1, value=1),
    html.P('Year range'),
    dcc.RangeSlider(id="year_range", min=1749, max=2023, step=1,
                    value=[1990, 2000], marks={1750: '1750', 1800: '1800', 1850: '1850',
                                               1900: '1900', 1950: '1950', 2000: '2000'}),

    # Question 2
    html.H4('Variability of Sunspot Cycle'),
    dcc.Graph(id="var_graph"),
    html.P('Select Variability: '),
    dcc.Slider(id="var_slider", min=1, max=20, step=1, value=11),

    # Question 3
    html.H4('Real-time NASA Solar Image'),
    dcc.Graph(id="sun_image"),
    dcc.Dropdown(id="sun_color",
                 options=['EIT 171', 'EIT 195', 'EIT 284', 'EIT 304',
                          'SDO/HMI Continuum', 'SDO/HMI Magnetogram', 'LASCO C2', 'LASCO C3'],
                 value='SDO/HMI Continuum',
                 clearable=False)
])


@app.callback(
    Output("graph", "figure"),
    Input("smoother", "value"),
    Input("year_range", "value")
)
def graph(smoother, y_range):
    # rolling allows smoothing with an integer of smoother, determined by slider
    # in an y_range, determined by range slider
    # source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
    df_s = cleaning(df_m.rolling(smoother).mean(), y_range)
    df = cleaning(df_m, y_range)

    # plots the line graph of monthly and smoothed data
    fig = go.Figure()
    monthly = go.Line(x=df['DecYear'], y=df['Gn'], name='monthly')
    smoothed = go.Line(x=df_s['DecYear'], y=df_s['Gn'], name='smoothed')

    # it's a matplotlib legend to graph-objects
    # source: https://plotly.com/python/creating-and-updating-figures/
    fig.add_trace(monthly)
    fig.add_trace(smoothed)
    return fig


def cleaning(df, y_range):
    # makes sure to only plot the data in year range
    return df[(df.DecYear > y_range[0]) & (df.DecYear < y_range[1])]


@app.callback(
    Output("var_graph", "figure"),
    Input("var_slider", "value")
)
def var_graph(var_s):
    # convert years into fractional year, determined by slider
    # and put it in another column
    df_m['VarYear'] = df_m['DecYear'] % var_s

    # plots the scatter plot of fractional year data
    var = px.scatter(x=df_m['VarYear'], y=df_m['Gn'])
    fig = go.Figure(var)
    return fig


@app.callback(
    Output("sun_image", "figure"),
    Input("sun_color", "value")
)
def current_sun(sun_color):
    # it plots an image as a graph-objects
    # source: https://plotly.com/python/imshow/
    img = io.imread(translation(sun_color))
    fig = px.imshow(img)
    return fig


def translation(sun_color):
    # image link shortcut
    sun = 'hmi_igr'
    if sun_color == 'EIT 171':
        sun = 'eit_171'
    elif sun_color == 'EIT 195':
        sun = 'eit_195'
    elif sun_color == 'EIT 284':
        sun = 'eit_284'
    elif sun_color == 'EIT 304':
        sun = 'eit_304'
    elif sun_color == 'SDO/HMI Magnetogram':
        sun = 'hmi_mag'
    elif sun_color == 'LASCO C2':
        sun = 'c2'
    elif sun_color == 'LASCO C3':
        sun = 'c3'
    return f'https://soho.nascom.nasa.gov/data/realtime/{sun}/1024/latest.jpg'


app.run_server(debug=True)
