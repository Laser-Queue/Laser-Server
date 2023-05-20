from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/games")
async def games():
    return "Not Implemented"

# GAME MANAGMENT

@app.get("/games/{game_id}")
async def get_game(game_id: str):
    return "Not Implemented"

@app.get("/games/{game_id}/players")
async def get_game_players(game_id: str):
    return "Not Implemented"

@app.post("/games/{game_id}/players")
async def add_game_players(game_id: str):
    return "Not Implemented"

# GAMEPLAY
@app.post("/games/{game_id}/players/{player_id}/tag")
async def tag_entity(game_id: str, player_id: str):
    return "Not Implemented"

