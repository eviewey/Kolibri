from sqlmodel import SQModel, Field
from typing import optional
class Driver (SQLModel, table=True):
id: Optional [int]=Field(default=None,primary_key=True)
name:str
license_number:str
truck_number:str
class Cargo (SQLModel, table=True):
id: Optional [int]=Field(default=None,primary_key=True)
name:str
destination:str
weight:float