# Flask Reference: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#implementing-our-api
# MongoDB-Flask Reference: https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application 
# New MongoDB-Flask Reference: https://stackabuse.com/integrating-mongodb-with-flask-using-flask-pymongo/ --> working example

import os
import shutil
from flask import json, jsonify, Flask, Response, render_template, request, url_for, redirect # render_template is only used to render an HTML template
from flask_pymongo import PyMongo
from script import run_steps as process_data
from csvConverter import convert as convert_to_dict
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app,resources={'/*':{'origins': 'http://localhost:3000'}})
app.config["DEBUG"] = True

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/payroll_db")
db = mongodb_client.db
records_collection = db.employee_records

@app.route('/', methods=['GET'])
def index():
    response = jsonify(message="Nice! It's running now! :)")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# route to upload file
@app.route('/upload', methods=['GET','POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def upload():       
    output = []    

    if request.method == 'POST':
        file = request.files['file']
        print("Posted file: {}".format(file))

        file_exists = db.time_report_files.find_one({"filename": file.filename})
        print("file_exists", file_exists)
        if file_exists == None:
            print("New File")
            # backs up the file itself to time_report_files collection
            mongodb_client.save_file(file.filename, file)
            db.time_report_files.insert_one({'filename': file.filename})            

            # process the csv
            target = "input"
            # delete input folder if existing
            print(target)
            if os.path.isdir(target) == True: shutil.rmtree(target)
            
            # create directory to save the file
            os.mkdir(target)
            save_location = os.path.join(target, file.filename)
            print(save_location)
            file.seek(0) # fixes the issue of Flask empty file when uploaded. Reference: https://stackoverflow.com/questions/62850956/flask-empty-files-when-uploaded
            file.save(save_location)
            
            # backs up each content of file to employee_records collection
            add_many(file.filename)

            # ensuring the output list is empty, then starts process the data.
            del output[:]
            output = process_data(save_location)
            response = app.response_class(
                response=json.dumps(output),
                status=209,
                mimetype='application/json'
            )
           
            return response
        else:
            print("File Exists")
            r = Response(response="File with that filename already exists", status=409)
            r.headers.add('Access-Control-Allow-Origin', '*')
            return r

    elif request.method == 'GET':
        return jsonify(output)


@app.route("/get_record/<int:eid>")
def insert_one(eid):
    records = []
    print("EID: " + str(eid))
    eid_records = records_collection.find({ 'employee id': eid })
    for document in eid_records:
        records.append(document)

    return jsonify(records), 200
    # return jsonify(message="success"), 200 

@app.route("/add_many")
def add_many(csv_file_path):
# def add_many():
#     csv_file_path = ('time-report-42.csv')
    starting_id = 1

    # check if collection exists
    list_of_collections = db.list_collection_names()  # Return a list of collections in 'test_db'
    print(list_of_collections)
    print(records_collection.name)
    if str(records_collection.name) in list_of_collections:
        print("contains")
        # find the last existing id and pass it to convert_to_dict
        max_id = records_collection.find({}).sort('_id', -1).limit(1)
        for document in max_id:
            max_id = document['_id']

        starting_id = max_id + 1

    records = records_collection.insert_many(convert_to_dict(csv_file_path,starting_id))

    return jsonify(message="success"), 200

app.run(host='0.0.0.0',port=5000)
