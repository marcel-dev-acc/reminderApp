# Django Web App Demonstration: Reminder App

The files and contents of the files have been created for express purpose of demonstrating how to initiate docker 
containers associated with a web app that manages customer reminder requests.

To run this project as a development package:
1) Please clone the repo
2) Navigate to the root folder that containers the Dockerfile


## Running the app for a full demonstration

Run the following commands in order:
- ```docker-compose build ```
- ```docker-compose up ```

You will notice that there are pending migrations that should be dealt with.

Stop the containers by either using the docker dashboard or using CTRL + C

- ```docker-compose run web python manage.py migrate ```
- ```docker-compose run web python manage.py createsuperuser ```

Go ahead and create a super user account to access the admin panel of Django

- ```docker-compose up ```

The app will return a database error if there is no user account in the database, to get around this error you will need to sign up the first account OR create an account in the admin panel of Django.

## Development

This project has a `Dockerfile` file.

```docker-compose build```

This project has a `docker-compose.yml` file.

```docker-compose up```


## Contributing

If you find typos or other issues with the guide, feel free to create a PR and suggest fixes!

If you have ideas on how to make the guide better or if you have new content, please open an issue first 
before working on your idea.
