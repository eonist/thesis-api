# thesis-api


## Setup
```bash
git clone https://github.com/olavblj/thesis-api.git
cd thesis-api
docker-compose up
```

When you run the project the first time, you have to make migrations before it will work. 
You do this by running `docker ps`, copying the container id of the api container, and running

```bash
docker exec -it [container id] bash
```

and then performing the migration just like with any other Django app.