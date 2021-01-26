from pydantic import BaseModel
from .proxy import Proxy

class Service(BaseModel):

    Kind: str
    ID: str
    Service: str
    Tags: list
    Meta: dict
    Port : int
    Address : str
    TaggedAddresses: dict
    Weights: dict
    EnableTagOverride: bool
    Datacenter: str
    ContentHash: str
    Proxy: Proxy
