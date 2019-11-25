#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Here's a quick example

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'), #H1 here is the header

    html.Div(children='''
        Dash: A web application framework for Python.
    '''), 

    dcc.Graph( #figure is the structure or dictionary where we have to put the data and the layout
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)

