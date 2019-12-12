# Simple test script (pytest + selenium)
The repository contains a sample of a test script using pytest and selenium web driver and GitHub as a tested app.

## Getting Started
Copy the repository from the GitHub and follow the instructions below.

### Prerequisites
Assure that you have installed:
* Python3 
* pip3
* geckodriver 0.26.0
 
#### Virtual Environment
Recommended way to use this script is with a virtual environment. Using `venv` which is avaiable by default in Python3, just type in a terminal:
``` sh
$ python3 -m venv venv
$ source venv/bin/activate
```
#### Geckodriver
Geckodriver is a driver for Firefox which is used in the test script. Choose a proper version for your distribution from [here](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0), install it and add its location to the environment variable `$PATH`.

#### Other dependencies
The necessary dependencies needed to run  tests are in the file `requirements.txt`. Install them with the command:
``` sh
$ pip3 install -r requirements.txt
```
### Configuration
Create a directory `variables/` and there create a file `login_data.json`. File should have the following contents:
```json
{
  "valid_username": "***",
  "valid_email": "***",
  "valid_password": "***",
  "invalid_password": "***"
}
```
Replace `***` with an appropriate data. 

## Running the script
Run all tests and load your data with the following command (in a root directory):
```sh
$ pytest --variables variables/login_data.json
```
