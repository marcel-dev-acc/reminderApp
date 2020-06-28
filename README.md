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

NB: The app will return a database error if there is no user account in the database, to get around this error you can do one fo the following:
1) Run the test script whch will automatically create the first user and submit the first scheduled message
2) Sign up the first account
3) Create an account in the admin panel of Django

## Development

This project has a `Dockerfile` file.

```docker-compose build```

This project has a `docker-compose.yml` file.

```docker-compose up```

## Selenium Tests

This project includes a scripted selenium test. The script runs using the chrome driver, which can be found in the zip file labelled "chromedriver_win32". Extract the chromedriver into the local folder and execute the file.
- On row 91 you will find the "CreateUser" function - this function creates a new user called 'user1'.
- On row 93 you will find the "LoginAsUser" function - this functions logs in as the user created in the previous function.
- On row 95 you will find the "ScheduleAMessage" function - this function adds a message to the task list.

## Contributing

If you find typos or other issues with the guide, feel free to create a PR and suggest fixes!

If you have ideas on how to make the guide better or if you have new content, please open an issue first 
before working on your idea.
