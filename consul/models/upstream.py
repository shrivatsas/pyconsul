from pydantic import BaseModel

class Upstream(BaseModel):

    DestinationType: str
    DestinationName: str
    LocalBindPort: int