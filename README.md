# iReporter


[![Build Status](https://travis-ci.org/chrismatgit/iReporter.svg?branch=tests)](https://travis-ci.org/chrismatgit/iReporter)				[![Coverage Status](https://coveralls.io/repos/github/chrismatgit/iReporter/badge.svg?branch=tests)](https://coveralls.io/github/chrismatgit/iReporter?branch=tests)				[![Maintainability](https://api.codeclimate.com/v1/badges/4675be29a4b16b20c98d/maintainability)](https://codeclimate.com/github/chrismatgit/iReporter/maintainability)



This is a web application that helps people to report incidents which can be a red-flag or incident.


## Getting Started

You can clone the project using the link [Github repository] (https://github.com/chrismatgit/iReporter.git) .

<!-- ## Prerequisites

The UI pages do not need much to be viewed as any web browser can view them from [this site](https://) as long as they have internet access. Please note that the UI is static at the moment as work is underway to connect the back-end to it. -->

## Installing

* Clone the project into your local repository using this command:

```sh
  $ git clone https://github.com/chrismatgit/iReporter.git
  ```
  Switch to the cloned directory, install a virtual environment, create a virtual environment, activate it, checkout to the most stable branch, install app dependencies and run the app.
  ```sh
    $ cd Store-Manager
    $ pip install virtualenv
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ git checkout ft-api
    $ pip install -r requirements.txt
    $ python3 run.py
 ```

**Note** If you're using Windows, activate your virtualenv using `` $ source venv/Scripts/activate ``
* Copy the url http://127.0.0.1:5000/ into your Postman and to run any endpoint follow the table under the heading (**Endpoints**) with the url prefix ('/api/v1') for each endpoint.

## Endpoints
HTTP Method | Endpoint | Functionality | Parameters | Protected
----------- | -------- | ------------- | ---------- | ---------
POST | /signup/ | Create a user | None | False
POST | /login/ | Login a user | None | False
GET | /welcome | Welcome a user | None | True
PATCH | /user/promote/int:user_id | Promote a user as an admin| user_id | False
GET | /users/ | Fetch all users | None | False
POST | /incident/ | Create an incident | None | False
GET | /incidents/int:incident_id | Fetch a single incident record | incident_id | False
GET | /incidents/| Fetch all incident records | None | False
PATCH | /incidents/incident_id/comment| Update a comment of a single incident record | None | False
PATCH | /incidents/incident_id/location| Update a location of a single incident record | None | False
DELETE | /incidents/incident_id| Delete a single incident record | incident_id | False


## Running the tests

Install pytest, source the .env file, run the tests.
```sh
  $ pip install pytest
  $ python3 -m pytest
  ```
## Deployment

The Python application is hosted on [Heroku](https://irepoter.herokuapp.com/api/v1/)


## Tools Used

* [Flask](http://flask.pocoo.org/) - Web microframework for Python
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python

## Built With

The project has been built with the following technologies so far:

<!-- * HTML
* CSS
* Javascript -->
* Python/Flask

## Contributions

To contibute to the project, create a branch from the **develop** branch and make a PR after which your contributions may be merged into the **develop** branch

## Authors

Christian Matabaro
