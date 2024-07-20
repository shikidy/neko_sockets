# Neko Socket
Your fluffy socket helper.

## Server setup

### Sync

```python
from neko_socket import NekoSocket


server = NekoSocket('localhost', 10205)

@server.dispatcher.bind_event('Template name', 1)
def template_callback(*data):
    print(f"Recieved data: {data}")

if __name__ = '__main__':
    server.thread_serve()
```