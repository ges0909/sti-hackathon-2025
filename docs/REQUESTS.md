# Examples for HTTP Requests with Python

This document shows how to perform HTTP requests in Python using the `requests` library.

## GET Request

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)
if response.status_code == 200:
    print(response.json())
```

## POST Request with JSON Data

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

## PUT Request

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    'id': 1,
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}
response = requests.put(url, json=data)
print(response.status_code)
print(response.json())
```

## DELETE Request

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.delete(url)
print(response.status_code)
```

## Working with Headers

```python
import requests

url = 'https://httpbin.org/get'
headers = {
    'Authorization': 'Bearer <TOKEN>'
}
response = requests.get(url, headers=headers)
print(response.json())
```

## Authentication Examples

### Basic Authentication

```python
import requests

url = 'https://httpbin.org/basic-auth/user/pass'
response = requests.get(url, auth=('user', 'pass'))
print(response.status_code)
print(response.json())
```

### Bearer Token Authentication

```python
import requests

url = 'https://httpbin.org/bearer'
headers = {
    'Authorization': 'Bearer YOUR_TOKEN_HERE'
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

### Custom Header Authentication

```python
import requests

url = 'https://httpbin.org/headers'
headers = {
    'X-API-KEY': 'your_api_key'
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

Further information: [Requests Documentation](https://docs.python-requests.org/en/latest/)
