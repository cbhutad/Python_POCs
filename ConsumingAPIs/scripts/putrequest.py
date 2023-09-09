import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

def putcall():
    """
        Performs a put http call to web url provided by API for JsonPlaceHolder. Here we first retrieve the resource current data using a get http call and pass the data value to be updated by replacing it in the json response.
    """

    response = requests.get(api_url)
    dataToPost = response.json()
    dataToPost["title"] = "Changed title"

    response = requests.put(api_url,json=dataToPost)
    print(response.json())
    print(f"Status code : {response.status_code}")