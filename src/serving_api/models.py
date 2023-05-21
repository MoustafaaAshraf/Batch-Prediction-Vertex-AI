from pydantic import BaseModel

class Data(BaseModel):
    instances: list = []
    parameters: dict = {}