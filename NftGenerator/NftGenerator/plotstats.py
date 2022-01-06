import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from metadata import Metadata



class PlotStats(object):

    metaArray = []
    app = object
        
    def read_dir(self, path):
        dir_list = os.listdir(path)
        print(dir_list)
        for file_name in dir_list:
            md = Metadata()
            file_name = path + file_name
            #print(file_name)
            md.read(file_name)
            self.metaArray.append(md)
            #print(md.get_name(), " ", md.get_image_url())
            del md
        return

    def plot(self):
        self.app = dash.Dash(__name__)

        min_damage = [10,20,30]
        max_damage = [40,50,60]

        rp = [100,200,500]

        ids = []

        for md in self.metaArray:
            ids.append(md.get_id())

        df = pd.DataFrame({
            "Min Damage": min_damage,
            "Max Damage": max_damage,
            "rp": rp,
            "id": ids,
        })

        fig = px.bar(df, x="Id", y="rp", barmode="group")
        self.app.layout = html.Div(children=[html.H1(children='Hello Dash'),
            html.Div(children='''
                Dash: A web application framework for your data.
            '''),
            dcc.Graph(id='example-graph-2',figure=fig),
            html.Div(children='''
                Dash: A web application framework for your data.
            '''),
            dcc.Graph(id='example-graph', figure=fig)])

        self.app.run_server(debug=True)
        return



