from pydantic import BaseModel
from typing import List

class TreeType(BaseModel):
    name: str
    color: str
    texture: str

    def draw(self, canvas, x: int, y: int):
        return {
            "name": self.name,
            "color": self.color,
            "texture": self.texture,
            "position": {"x": x, "y": y}
        }

class Tree(BaseModel):
    x: int
    y: int
    type: TreeType

    def draw(self, canvas):
        return self.type.draw(canvas, self.x, self.y)

class Forest(BaseModel):
    trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str, factory):
        tree_type = factory.get_tree_type(name, color, texture)
        tree = Tree(x=x, y=y, type=tree_type)
        self.trees.append(tree)
        return tree

    def draw(self, canvas):
        return [tree.draw(canvas) for tree in self.trees]
