
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE


POST /sort-names


GET /names?add=Eddie,Leo



```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

names = Joe,Alice,Zoe,Julia,Kieran
returns Alice,Joe,Julia,Kieran,Zoe

names = Alice, Julia, Karim
add = Eddie, Leo
returns Alice, Eddie, Julia, Karim, Leo

```



## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

def test_sort_names(web_client):
    web_client.post('/sort_names', data={'text': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'



 /names?add=Eddie,Leo

 def test_add(web_client):
    web_client.get('/names', data={'names':'Eddie,Leo'})
    assert response.status_code == 200
    names = 'Alice,Bob,Charlie'
    assert response.data.decode('utf-8') = 'Alice,Bob,Charlie,Eddie,Leo'

 ```