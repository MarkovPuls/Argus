from pydantic import BaseModel, Field
from typing import List, Union
from datetime import datetime


class Planet(BaseModel):
    name: str
    rotation_period: Union[int, str] = Field(..., description="Length of planet day in hours")
    orbital_period: Union[int, str] = Field(..., description="Time to orbit its star in days")
    diameter: Union[int, str]
    climate: str
    gravity: str
    terrain: str
    surface_water: Union[int, str]
    population: Union[int, str]
    residents: List[str] = Field(..., description="List of resident URLs")
    films: List[str] = Field(..., description="List of film URLs")
    created: datetime
    edited: datetime
    url: str
