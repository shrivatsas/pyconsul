import requests
import service

class Agent:

    def __init__(self, 
        hostAndPort: Set[Tuple(str, str)] = {("127.0.0.1", "8500")}, 
        timeoutMillis: long = 60000):
        self.hostAndPort = hostAndPort
        self.timeoutMillis = timeoutMillis

    def register(self, service: Service):
        print("hello")
