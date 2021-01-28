from consul.models.service import Service
from consul.agent import Agent

def test_serviceSchema():
    serv = Service.parse_file("tests/data/sampleOne.json")
    print(serv)

def test_agentConnect():
    ag = Agent()
    print(ag.hosts.get('127.0.0.1:8500'))

def test_serviceRegister():
    serv = Service.parse_file("tests/data/sampleOne.json")
    ag = Agent()
    ag.register(serv)