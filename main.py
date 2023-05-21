'''
    Laserv
    The laser tag system manager.
    Joel DeSante 2023
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "name": "Laserv",
        "description": "Laser tag system managment software.",
        "version": "1.0.0",
        "author": "Joel DeSante"
    }

# PACK MANAGMENT
@app.get("/packs")
async def packs():
    return "Not Implemented"

@app.post("/packs")
async def register_packs():
    return "Not Implemented"

@app.get("/packs/{pack_id}")
async def pack(pack_id: str):
    return "Not Implemented"

@app.delete("/packs/{pack_id}")
async def delete_pack(pack_id: str):
    return "Not Implemented"

# GAME MANAGMENT
@app.get("/games")
async def games():
    return "Not Implemented"

@app.get("/games/{game_id}")
async def game(game_id: str):
    return "Not Implemented"

@app.get("/games/{game_id}/players")
async def game_players(game_id: str):
    return "Not Implemented"

@app.post("/games/{game_id}/players")
async def add_game_players(game_id: str):
    return "Not Implemented"

@app.delete("/games/{game_id}/players/{player_id}")
async def delete_game_players(game_id: str, player_id: str):
    return "Not Implemented"

# GAMEPLAY
@app.post("/games/{game_id}/players/{player_id}/tag")
async def tag_entity(game_id: str, player_id: str):
    return "Not Implemented"
