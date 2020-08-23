# sciapi
The PokeApi for nerds that truly love science


## How to Run:
To run the project locally is very easy.  
1. First you need to clone the repository on your local environment.  
`git clone https://github.com/pedrocecchetti/sciapi.git `  
2. Just enter into the directory and run
`docker-compose up -d `  
This will set up the containers and everything you need to run the simplest version of this api
3. After that you need to execute the migrations to structure your database. Remeber to change the __container_id__ to the web service container id  
`docker exec -it <container_id> alembic upgrade head`
4. You are good to go!  Just visit the documentation at `/docs` to see the summary of all endpoints and play with it!