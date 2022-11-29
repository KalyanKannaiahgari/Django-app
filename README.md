# This project contains sample Django code

# Prerequisites for running the project
### 
* Python needs to be installed
* pip needs to be installed


# Steps for configuring the project
After downloading the project, go inside the folder. <br/>
### 
* As part of the project, it is good to have a separate runtime environment for running Django. It is an optional step only. Command to install is **`python -m pip install pipenv`** <br/>
* Then to go inside of environment use **`pipenv shell`** <br/>
<br/>
<br/>
* If **`pipenv`** is not installed just install django using **`pip install django`**<br/>

# Step for running the project using<br/> 
**`python manage.py runserver`** <br/>

By default, it will run the application using the **8000** port. <br/>
Suppose we need to run in custom port means, then execute below <br/>
**`python manage.py runserver 8001`** <br/>

## Project gives below urls <br/>
[http://127.0.0.1:8000/app/welcome/](http://127.0.0.1:8000/app/welcome/) - Returns JSON  <br/>
[http://127.0.0.1:8000/app/welcome-template/](http://127.0.0.1:8000/app/welcome-template/) - Returns HTML using template
