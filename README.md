# Payroll Generator


## Installation and Running the Application (Mac)
**Backend - Python3 + Flask**

1. Install python3 and pip3

2. Install flask, pymongo, flask-PyMongo, Flask-Cors using pip3
```
pip3 install Flask
pip3 install pymongo
pip3 install Flask-PyMongo
pip3 install Flask-Cors
```
3. In `backend/api` directory:
```sh
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
4. The flask server should now be accessible through `localhost:5000`.

**Database - MongoDB Compass**

1. Download MongoDB Compass.
2. Setup new connection with `URI - mongodb://localhost:27017`

**Frontend - React Typescript + TailwindCSS**

1. In `frontend` directory:
```sh
npm install
yarn start
```
2. The web application should now be accessible through `localhost:3000`.
