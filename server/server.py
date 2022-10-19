from fastapi import FastAPI
from routers import pokemons_api, trainers_api
import uvicorn

app = FastAPI()
app.include_router(pokemons_api.router)
app.include_router(trainers_api.router)


@app.get("/")
def root():
    return "server is running"


# if __name__ == "__main__":
#     uvicorn.run("server:app", host="localhost", port=8000, reload=True)
