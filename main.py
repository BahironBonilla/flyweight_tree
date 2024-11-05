from fastapi import FastAPI
from models import Forest
from tree_factory import TreeFactory
from data import forest, factory

app = FastAPI()

@app.post("/plant_tree/")
async def plant_tree(x: int, y: int, name: str, color: str, texture: str):
    tree = forest.plant_tree(x, y, name, color, texture, factory)
    return {"message": "Tree planted", "tree": tree}

@app.get("/draw_forest/")
async def draw_forest():
    canvas = {}
    return {"forest": forest.draw(canvas)}
