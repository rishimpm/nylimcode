import flask
app = flask.Flask(__name__)

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    custom_headers = flask.request.headers
    print("Received Headers:")
    for header, value in custom_headers.items():
        print(f"{header}: {value}")
    
    custom_header_value = flask.request.headers.get('X-Aws-Role-Name')
    if custom_header_value:
        print(f"X-Aws-Role-Name header value: {custom_header_value}")
    else:
        print("X-Aws-Role-Name header not found")

    custom_header_value = flask.request.headers.get('X-Email')
    if custom_header_value:
        print(f"X-Email header value: {custom_header_value}")
    else:
        print("X-Email header not found")

    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)