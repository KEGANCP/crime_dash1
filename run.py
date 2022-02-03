import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask 

# Imports from this application
from app import app, server
from pages import index, predictions, GitHub, tableau

# Navbar 
navbar = dbc.NavbarSimple(
    brand='Predicting Crime in Chicago',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('GitHub', href='/GitHub', className='nav-link')), 
        dbc.NavItem(dcc.Link('Tableau', href='/tableau', className='nav-link'))
    ],
    sticky='top',
    color='dark', 
    light=False, 
    dark=True
)

footer = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Crime Prediction Team
                    Kegan Propster
                    Sean Farr
                    Austen Marden
            """
        ),
        
    ],
    md=4,
)


# footer = dbc.Container(
#     dbc.Row(
#         dbc.Col(
#             html.P(
#                 [
#                     html.Span('Crime Prediction Team', className='mr-2'), 
#                     html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:antonio.j.peterson@gmail.com'), 
#                     html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/ChicagoDataScientist/chicago-crime'),
#                     html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/petersonaj/'), 
#                     html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/DataScienceTony'), 
#                 ], 
#                 className='lead'
#             )
#         )
#     )
# )

# Layout 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(),
    footer
])


# URL Routing
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/GitHub':
        return GitHub.layout
    elif pathname == '/tableau':
        return tableau.layout       
    else:
        return dcc.Markdown('## Page not found')

# Run app server
if __name__ == '__main__':
    app.run_server(debug=True)


