import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import torch

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>My First Deployed Application</h1><p>This is my first deployed application</p>"

@app.route('/api/v1/text', methods=['GET'])
@cross_origin()
def text_call():
    code  = request.args.get('code', None)
    epochs  = request.args.get('epochs', None)
    class_num = request.args.get('class',None)
    max_len = request.args.get('maxlen', None)
    return jsonify([code, epochs,class_num, max_len])
@app.route('/api/v1/image', methods=['GET'])
@cross_origin()
def img_call():
    code  = request.args.get('code', None)
    epochs  = request.args.get('epochs', None)
    class_num = request.args.get('class',None)
    hei = request.args.get('height', None)
    wid = request.args.get('width', None)
    return jsonify([code, epochs,class_num,hei, wid])
    
@app.route('/api/v1/echo', methods=['GET'])
@cross_origin()
def prof_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    echo = ""
    if 'echo' in request.args:
        echo = (request.args['echo'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = "loud and clear: "+ echo

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/api/v1/torch', methods=['GET'])
@cross_origin()
def torch_call():

    result = str(torch.version)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)