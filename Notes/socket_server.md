# Socket Programming in python


### Server.py
```python

import socket

s = socket.socket()

print("socket created")

s.bind(('localhost',9999))

s.listen()
print("waiting for connections")

while True:
	c, addr = s.accept()
	name = c.recv(1024).decode()
	print("Connected with ", addr, name)

	c.send(bytes("Welcome to vashishth pc",'utf-8'))

	c.close()

#output :-

# socket created
# waiting for connections
# Connected with  ('127.0.0.1', 60562) vasu
# Connected with  ('127.0.0.1', 60564) jay
# Connected with  ('127.0.0.1', 60566) shailesh

```

### client.py

```python

import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your name : ")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())

```