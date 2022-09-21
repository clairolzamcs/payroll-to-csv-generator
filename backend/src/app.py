from flask import Flask, request, url_for, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/payroll'
mongo = PyMongo(app)

CORS(app)

@app.route('/upload', method=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
    return 'test'
   


if __name__ == '__main__':
    app.run(debug=True)