# sciapi
Yeah, I kno , it's pretty nice to see ho stubborn Charizard is and which abilities he has.  
Yeah, I agree that Slopoke is the best Pokemon ever and that Misty was always better than Ash and Brock.  
I am also indeed a fan of Pokemon, but wait, don't you think that the worlds most famous minds deserve their place in a
beautiful API?

#### THAT'S THE REASON FOR CREATING SciAPI!

- Now your hours learning development will aggregate to your knowledge!
- You are gonna see how your nationality changed worlds history!
- Now you're gonna really understand **what the heck** is the Schrödinger's cat.


## How to Run:
To run the project locally is very easy.  
1. First you need to clone the repository on your local environment.  
`git clone https://github.com/pedrocecchetti/sciapi.git `  
2. Just enter into the directory and run
`docker-compose up -d `  
This will set up the containers and everything you need to run the simplest version of this api
3. After that you need to execute the migrations to structure your database. Remember to change the __container_id__ to the web service container id  
`docker exec -it <container_id> alembic upgrade head`
4. You are good to go!  Just visit the documentation at `/docs` to see the summary of all endpoints and play with it!