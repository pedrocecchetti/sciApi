from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "456 to UAU!"}