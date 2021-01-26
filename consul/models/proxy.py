from pydantic import BaseModel
from typing import List
from . import Upstream

class Proxy(BaseModel):

    DestinationServiceName: str
    DestinationServiceID: str
    LocalServiceAddress: str
    LocalServicePort: int
    Config: dict
    Upstreams: List[Upstream]
