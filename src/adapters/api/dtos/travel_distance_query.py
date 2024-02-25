from pydantic import BaseModel

class TravelDistanceQuery(BaseModel):
    origin: str
    destination: str
