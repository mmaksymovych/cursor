from flask import Flask, render_template, request, jsonify
import plotly
import plotly.express as px
import json
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Create initial sample data using pandas
    df = pd.DataFrame({
        'x': range(10),
        'y': [i * 2 for i in range(10)]
    })
    
    # Create a simple line plot
    fig = px.line(df, x='x', y='y', title='Sample Line Graph')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', graphJSON=graphJSON)

@app.route('/update_graph', methods=['POST'])
def update_graph():
    data = request.get_json()
    values = data.get('values', [])
    
    # Create DataFrame from the provided values
    df = pd.DataFrame({
        'x': range(len(values)),
        'y': values
    })
    
    # Create new graph with the provided values
    fig = px.line(df, x='x', y='y', title='Updated Line Graph')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return jsonify({'graph': graphJSON})

if __name__ == '__main__':
    app.run(debug=True) 