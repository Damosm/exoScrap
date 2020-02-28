import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df = pd.read_csv(r"C:\Users\utilisateur\Documents\Python\Scraping\Briefs_projet.csv",
                   dtype={"fips": str})
# Enlever espace ds la colonne rang
df['rang'] = df['rang'].str.strip()

#selects
df1 = df[(df.rang=='1')&(df.Sexe=='M')][['Annee','Performances','Noms']]
df2 = df[(df.rang=='1')&(df.Sexe=='W')][['Annee','Performances','Noms']]

#################################""
fig = go.Figure(data=[go.Scatter(x=df1['Annee'], y=df1['Performances'])])
fig2 = go.Figure(data=[go.Scatter(x=df2['Annee'], y=df1['Performances'])])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Triple Saut Masculin de 1891 à 2019'),
    dcc.Graph(
        id='Perf',
        figure=fig
    ),
    html.Div(children=[
        html.H1(children='Triple Saut Feminin de 1891 à 2019'),
        dcc.Graph(
            id='Perf2',
            figure=fig2
        )
    ])
    
])


if __name__ == '__main__':
    app.run_server(debug=True)
#####################################################################""