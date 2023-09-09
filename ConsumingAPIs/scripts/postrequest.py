import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

def postcallnoheaders():
    """ 
        Performs a post http call to web url provided by API for JsonPlaceHolder. Here we have to provide the data for resource to be created. The example demostrates this for json format without specifying the headers with Content-type information explicitly. The Content-Type is set by post() and it also serializes the data to be added and adds to the body of request.
    """

    dataToPost = {
        "userId": 1,
        "title": "Studying requests Module",
        "completed": "false"
    }

    response = requests.post(api_url,json=dataToPost)
    print(response.json())
    print(f"Status code : {response.status_code}")
    print(f"Content-Type : {response.headers['Content-Type']}")
    
def postcallheaders():
    """ 
        Performs a post http call to web url provided by API for JsonPlaceHolder. Here we have to provide the data for resource to be created. The example demostrates this for json format with specifying the headers with Content-type information explicitly.
    """

    dataToPost = {
        "userId": 2,
        "title": "Studying requests post module",
        "completed": "false" 
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, data=json.dumps(dataToPost), headers=headers)
    print(response.json())
    print(f"Status Code : {response.status_code}")
    print(f"Content-type : {response.headers['Content-Type']}")