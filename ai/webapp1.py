import dash
from dash import html

# Create Dash application
docsapp = dash.Dash(__name__, requests_pathname_prefix='/documentsummarizer/')
server = docsapp.server

docsapp.layout = html.Div([
    html.H1("Web App 11"),
    html.P("This is the first web application.")
])

if __name__ == '__main__':
    docsapp.run_server(debug=True)
