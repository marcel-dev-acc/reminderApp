# Django Web App Demonstration: Reminder App

The files and contents of the files have been created for express purpose of demonstrating how to initiate docker 
containers associated with a web app that manages customer remind requests.
To run this project as a development package:
1) Please clone the repo
2) Navigate to the root folder that containers the Dockerfile


## Running the app for a full demonstration

Run the following commands in order:
- ```bash docker-compose build ```
- ```bash docker-compose up ```

You will notice that there are pending migrations that should be dealt with.
Stop the containers by either using the docker dashboard or using CTRL + C

- ```bash docker-compose run web python manage.py migrate ```
- ```bash docker-compose run web python manage.py createsuperuser ```
- ```bash docker-compose up ```


## Development

This project has a `Dockerfile` file.

```bash
docker-compose build
```

This project has a `docker-compose.yml` file.

```bash
docker-compose up
```


## Contributing

If you find typos or other issues with the guide, feel free to create a PR and suggest fixes!

If you have ideas on how to make the guide better or if you have new content, please open an issue first 
before working on your idea.
