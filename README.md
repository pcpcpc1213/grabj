# grabj
This Python module (made on 3.7.2) grabs JSON data quickly through 2 arguments, 'url' and 'call'.
Usage:
```python
grabj.getjson(url="url here", call="call here")
```
Example:

```python
>>> import grabj
>>> title = None
>>> source = "https://jsonplaceholder.typicode.com/todos/1"
>>> grabj.getjson(url=source, call="title")
>>> print(title)
delectus aut autem
```


