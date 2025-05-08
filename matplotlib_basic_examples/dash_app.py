import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

# List of all graph types
GRAPH_TYPES = [
    # Simple
    "Line Plot",
    "Scatter Plot",
    "Bar Plot",
    "Histogram",
    "Pie Chart",
    # Medium
    "Stacked Bar Plot",
    "Box Plot",
    "Violin Plot",
    "Multiple Lines",
    "Heatmap",
    # Advanced
    "3D Surface Plot",
    "Polar Plot",
    "Contour Plot"
]

app.layout = html.Div([
    html.H1("Interactive Graph Explorer"),
    dcc.Dropdown(
        id='graph-type',
        options=[{"label": name, "value": name} for name in GRAPH_TYPES],
        value='Line Plot',
        style={'width': '50%'}
    ),
    html.Div(id='controls-container'),
    dcc.Graph(id='main-graph')
])

# Dynamic controls based on graph type
@app.callback(
    Output('controls-container', 'children'),
    Input('graph-type', 'value')
)
def update_controls(name):
    controls = []
    if name == "Line Plot":
        controls = [
            html.Label("Frequency:"),
            dcc.Slider(id='freq', min=0.1, max=5, step=0.1, value=1, marks={i: str(i) for i in range(1, 6)})
        ]
    elif name == "Scatter Plot":
        controls = [
            html.Label("Number of Points:"),
            dcc.Slider(id='npoints', min=10, max=500, step=10, value=100, marks={i: str(i) for i in range(50, 501, 50)})
        ]
    elif name == "Bar Plot":
        controls = [
            html.Label("Bar Values:"),
            dcc.Input(id='bar-values', value='10,24,36,18', type='text')
        ]
    elif name == "Histogram":
        controls = [
            html.Label("Number of Bins:"),
            dcc.Slider(id='bins', min=5, max=50, step=1, value=30, marks={i: str(i) for i in range(5, 51, 5)})
        ]
    elif name == "Pie Chart":
        controls = [
            html.Label("Values (comma separated):"),
            dcc.Input(id='pie-values', value='15,30,45,10', type='text')
        ]
    # For medium/advanced, you can add more controls as needed
    return controls

# Main graph callback
@app.callback(
    Output('main-graph', 'figure'),
    [
        Input('graph-type', 'value'),
        Input('freq', 'value'),
        Input('npoints', 'value'),
        Input('bar-values', 'value'),
        Input('bins', 'value'),
        Input('pie-values', 'value')
    ]
)
def update_graph(name, freq, npoints, bar_values, bins, pie_values):
    fig = go.Figure()
    # Simple
    if name == "Line Plot":
        x = np.linspace(0, 10, 100)
        y = np.sin((freq or 1) * x)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'sin({freq}x)'))
        fig.update_layout(title="Line Plot", xaxis_title="x", yaxis_title="sin(x)")
    elif name == "Scatter Plot":
        n = npoints or 100
        x = np.random.rand(n)
        y = np.random.rand(n)
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
        fig.update_layout(title="Scatter Plot")
    elif name == "Bar Plot":
        try:
            values = [int(v) for v in (bar_values or '10,24,36,18').split(',')]
        except Exception:
            values = [10, 24, 36, 18]
        categories = [chr(65+i) for i in range(len(values))]
        fig.add_trace(go.Bar(x=categories, y=values))
        fig.update_layout(title="Bar Plot")
    elif name == "Histogram":
        data = np.random.randn(1000)
        fig.add_trace(go.Histogram(x=data, nbinsx=bins or 30))
        fig.update_layout(title="Histogram")
    elif name == "Pie Chart":
        try:
            values = [int(v) for v in (pie_values or '15,30,45,10').split(',')]
        except Exception:
            values = [15, 30, 45, 10]
        labels = [chr(65+i) for i in range(len(values))]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title="Pie Chart")
    # Medium
    elif name == "Stacked Bar Plot":
        categories = ['A', 'B', 'C', 'D']
        values1 = [10, 20, 30, 40]
        values2 = [5, 15, 25, 35]
        fig.add_trace(go.Bar(x=categories, y=values1, name='Set 1'))
        fig.add_trace(go.Bar(x=categories, y=values2, name='Set 2'))
        fig.update_layout(barmode='stack', title="Stacked Bar Plot")
    elif name == "Box Plot":
        data = [np.random.normal(0, std, 100) for std in range(1, 4)]
        for i, d in enumerate(data):
            fig.add_trace(go.Box(y=d, name=f'Set {i+1}'))
        fig.update_layout(title="Box Plot")
    elif name == "Violin Plot":
        data = [np.random.normal(0, std, 100) for std in range(1, 4)]
        for i, d in enumerate(data):
            fig.add_trace(go.Violin(y=d, name=f'Set {i+1}'))
        fig.update_layout(title="Violin Plot")
    elif name == "Multiple Lines":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='sin(x)'))
        fig.add_trace(go.Scatter(x=x, y=np.cos(x), mode='lines', name='cos(x)'))
        fig.update_layout(title="Multiple Lines")
    elif name == "Heatmap":
        data = np.random.rand(10, 10)
        fig = go.Figure(data=go.Heatmap(z=data, colorscale='Viridis'))
        fig.update_layout(title="Heatmap")
    # Advanced
    elif name == "3D Surface Plot":
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
        fig.update_layout(title="3D Surface Plot")
    elif name == "Polar Plot":
        theta = np.linspace(0, 2 * np.pi, 100)
        r = np.abs(np.sin(5 * theta))
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=r, theta=np.degrees(theta), mode='lines'))
        fig.update_layout(title="Polar Plot")
    elif name == "Contour Plot":
        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.exp(-X**2 - Y**2)
        fig = go.Figure(data=go.Contour(z=Z, x=x, y=y))
        fig.update_layout(title="Contour Plot")
    return fig

if __name__ == '__main__':
    app.run(debug=True) 