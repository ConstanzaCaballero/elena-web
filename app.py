import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = render_template('index.html')
    from flask import make_response
    resp = make_response(response)
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
