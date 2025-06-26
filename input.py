from pydantic import BaseModel

class PassengerData(BaseModel):
    pclass: int
    sex: str
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: str
    alone: bool