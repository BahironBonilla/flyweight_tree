from models import TreeType
from typing import List

class TreeFactory:
    tree_types: List[TreeType] = []

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        for tree_type in cls.tree_types:
            if tree_type.name == name and tree_type.color == color and tree_type.texture == texture:
                return tree_type
        new_tree_type = TreeType(name=name, color=color, texture=texture)
        cls.tree_types.append(new_tree_type)
        return new_tree_type
