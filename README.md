#### django-starter-boilerplate including Environment settings - A django begginer boilerplate that ensure seemless deployment to Heroku

### Configuration Instructions

* Install the required packages in your virtual environment by running the below command:

```sh
pip install -r requirements.txt
```

* If you wont be using this project name, kindly edit the project name in the Procfile and wsgi file and all other possible occurences. 

### Heroku Settings

* Run the below commands to create the free plan of postgresql db on heroku

```sh
heroku addons:create heroku-postgresql:hobby-dev
```
### For development environment usage

* Navigate to the `.env` file in the root dir. 

Ensure the ENV_NAME = 'dev'.

### For production environment usage

* Navigate to the `.env` file in the root dir. 

Ensure the ENV_NAME = 'prod'.

# To get a better result. It is encouraged that you use the file and folder structure as represented on this repo.
