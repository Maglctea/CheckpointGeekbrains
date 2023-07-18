import json
from pydantic import BaseModel


def save_json(obj: dict, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(obj, file, default=str)


def load_json(filename: str) -> dict:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
