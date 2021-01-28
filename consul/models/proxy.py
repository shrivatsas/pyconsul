from pydantic import BaseModel, Field
from typing import List
from .upstream import Upstream

class Proxy(BaseModel):

    DestinationServiceName: str
    DestinationServiceID: str
    LocalServiceAddress: str
    LocalServicePort: int
    ProxyConfig: dict = Field(alias='Config')
    Upstreams: List[Upstream]
