import httpx
from consul.models.service import Service

class Agent:

    hosts = {}

    def __init__(self, 
        hostAndPort: set[str] = {("127.0.0.1:8500")}, 
        timeoutMillis: int = 60000):
        hostAndPort = hostAndPort
        self.timeoutMillis = timeoutMillis

        for host in hostAndPort:
            res = httpx.head(f"http://{host}")
            self.hosts[f"{host}"] = (res.status_code == 200)

    def register(self, service: Service):
        ENDPOINT = "/v1/agent/service/register"
        httpx.post(ENDPOINT, data=service)

    def deregister(self, service_id: str):
        ENDPOINT = f"/v1/agent/service/deregister/{service_id}"
        httpx.post(ENDPOINT)

    def enableMaintenance(self, service_id: str, enable: bool, reason: str):
        ENDPOINT = f"/v1/agent/service/maintenance/{service_id}?enable={enable}&reason={reason}"
        httpx.post(ENDPOINT)