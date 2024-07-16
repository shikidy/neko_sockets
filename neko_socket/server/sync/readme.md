# Connect
Server: 110 121 97

# Transform bind and data

## Server

from pydantic import BaseClass

class TestData(BaseClass):
    name: str
    value: str

@s.bind("event_name", id=1)
def callback(data: dict):
    ...
    
event_name  < 3 bytes


## Client

s.send(1, {
    "name": "my_name",
    "value": "value"
})

-> 1

