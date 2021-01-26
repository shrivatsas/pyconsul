import httpx
import service

class Agent:

    hosts = {}

    def __init__(self, 
        hostAndPort: Set[str] = {("127.0.0.1:8500")}, 
        timeoutMillis: long = 60000):
        hostAndPort = hostAndPort
        self.timeoutMillis = timeoutMillis

        for host in hostAndPort:
            res = httpx.head("https://source.unsplash.com/random")
            self.hosts["host"] = res.status_code

    def register(self, service: Service):
        print("hello")
