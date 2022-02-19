import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# tables 
classes_db = [['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112'], ['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110'], ['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112'], ['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112'], ['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', ''], ['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110']]

professor_db = {'Trucke': [['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112']], 'Rosenbaum': [['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112']], 'Valentine': [['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112']], 'Mackalski': [['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112']], 'Pressler': [['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112']], 'Nelson': [['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112']], 'Firestone': [['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110']], 'Aldrich': [['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112']], 'Keck': [['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', '']], 'Perlman': [['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', '']], 'Antonson': [['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH']], 'Beck': [['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110']]}
credit_db = {'4': [['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110'], ['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112'], ['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112'], ['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112']], '1': [['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112']], '3': [['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110'], ['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', ''], ['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112'], ['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112']]}
days_of_week_db = {'MW': [['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112'], ['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112']], 'MWF': [['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', ''], ['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112']], 'TR': [['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110'], ['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112'], ['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110'], ['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112']], 'F': [['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112']], 'W': [['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112']]}
room_db = {'KAUF_112': [['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112'], ['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112'], ['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112'], ['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112']], 'KAUF_110': [['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110'], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', ''], ['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110']], 'KAUF_GH': [['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH']]}
time_db = {'10:30AM-11:45AM': [['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Mackalski', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_185H', '9762', 'FOUNDATIONS_OF_LEADERSHIP_I', 'Valentine', '1', 'F', '10:30AM-11:45AM', 'KAUF_112'], ['RAIK_181H', '9749', 'FOUNDATIONS_OF_ACCOUNTING', 'Trucke', '4', 'MW', '10:30AM-11:45AM', 'KAUF_112']], '12:30PM-2:20PM': [['RAIK_182H', '9746', 'FOUNDATIONS_OF_ECONOMICS', 'Rosenbaum', '4', 'MWF', '12:30PM-2:20PM', 'KAUF_112']], '11:00AM-12:50PM': [['RAIK_184H', '9733', 'SOFTWARE_DEVELOPMENT_ESSENTIALS', 'Valentine', '4', 'TR', '11:00AM-12:50PM', 'KAUF_112']], '3:30PM-4:45PM': [['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Nelson', '1', 'W', '3:30PM-4:45PM', 'KAUF_112'], ['RAIK_186H', '9809', 'FOUNDATIONS_OF_LEADERSHIP_II', 'Pressler', '1', 'W', '3:30PM-4:45PM', 'KAUF_112']], '3:30PM5:20PM': [['RAIK_284H', '19875', 'SOFTWARE_ENGINEERING_IV', 'Firestone', '4', 'TR', '3:30PM5:20PM', 'KAUF_110']], '5:00PM-6:15PM': [['RAIK_288H', '9785', 'HONORS_BUSINESS_WRITING', 'Aldrich', '3', 'MW', '5:00PM-6:15PM', 'KAUF_112']], '9:30AM-10:45AM': [['RAIK_371H', '9767', 'DATA_&_MODELS_III', 'Keck', '3', 'TR', '9:30AM-10:45AM', 'KAUF_110', ''], ['RAIK_341H', '9810', 'MARKETING', 'Mackalski', '3', 'TR', '9:30AM-10:45AM', 'KAUF_112']], '10:30AM-11:20AM': [['RAIK_370H', '9758', 'DATA_AND_MODELS_II', 'Keck', '3', 'MWF', '10:30AM-11:20AM', 'KAUF_110', '']], '11:30AM-12:20PM': [['RAIK_372H', '9763', 'BUSINESS_LAW', 'Perlman', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', ''], ['RAIK_372H', '9763', 'BUSINESS_LAW', 'Firestone', '3', 'MW', '11:30AM-12:20PM', 'KAUF_110', '']], '2:00PM-3:15PM': [['RAIK_404H', '9759', 'RAIK_DESIGN_STUDIO_IV', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH'], ['RAIK_402H', '9734', 'RAIK_DESIGN_STUDIO_II', 'Antonson', '3', 'TR', '2:00PM-3:15PM', 'KAUF_GH']], '11:00AM-12:15PM': [['RAIK_476H', '9811', 'BUSINESS_POLICIES_AND_STRATEGIES', 'Beck', '3', 'TR', '11:00AM-12:15PM', 'KAUF_110']]}


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>My First Deployed Application</h1><p>This is my first deployed application</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/spring/all', methods=['GET'])
@cross_origin()
def api_all():
    return jsonify(classes_db)

@app.route('/api/v1/resources/spring/professor', methods=['GET'])
@cross_origin()
def prof_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    professor = ""
    if 'professor' in request.args:
        professor = (request.args['professor'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = professor_db[professor]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/api/v1/resources/spring/credit', methods=['GET'])
@cross_origin()
def cred_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    credit = ""
    if 'credit' in request.args:
        credit = (request.args['credit'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = credit_db[credit]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/api/v1/resources/spring/days', methods=['GET'])
@cross_origin()
def days_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    day = ""
    if 'day' in request.args:
        day = (request.args['day'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = days_of_week_db[day]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)


@app.route('/api/v1/resources/spring/room', methods=['GET'])
@cross_origin()
def room_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    room = ""
    if 'room' in request.args:
        room = (request.args['room'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = room_db[room]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/api/v1/resources/spring/time', methods=['GET'])
@cross_origin()
def time_call():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    time = ""
    if 'time' in request.args:
        time = (request.args['time'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = time_db[time]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)