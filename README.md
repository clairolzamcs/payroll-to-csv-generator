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

### How did you test your implementation was correct?
I used microsoft excel to compute the expected correct values for each employee per cut off. I multiply the hours worked to the wage based on the job group, then I get the total amount per cut off based on the date. In creating the JSON response, the hierarchy was based on the employee ID and pay period.

### If this application was destined for a production environment, what would you add and change?

1. The business logic that I have right now is just ahappy path, so if this is for production environment, I will put some sort of callbacks to handle errors/exceptions. 
2. The security and authentication of data in transit and data at rest. 
3. Performance of the application, I will add more testing and run a unit testing for the whole application and modify it to be able to handle multiple requests at the same time. Perhaps, executing a performance testing prior to the deploymen in production. 
4. To hava a uniform API across the entire application using GraphQL. 
5. I'll add more logging for observability so troubleshooting will be easier.

### What compromises did you have to make as a result of the time constraints of this challenge?
1. I'll work on refining the flawed logic behind how the values are computed. After the system receives the file from the client-side, it backs up the file itself and inserts each content to the database and then, process the file. I therefore intend to improve it by processing the records inside the database rather than the file as I would need to extract data across all uploaded time reports, not just those from the recently uploaded one. However, I created an endpoint that can extract all records for a specific employee accross all time reports` /get_record/{employee_id}`.
2. Although uploading of duplicate is being caught in the server side (returns status code: 409), It is not being reflected in the client-side as the validations are not implemented there yet. 
3. Database was plain and simple.
4. I chose MongoDB because it is easier to setup but since we store sensitive data and currently the database are not authenticated, therefore I'll probably switch to a more scalable and secured database, such AWS RDS. 
