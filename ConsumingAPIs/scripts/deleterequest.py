import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

def deletecall():
    """
        Perform delete http call to url provided by API for free web service JSONPlaceholder.
    """
    response = requests.delete(api_url)
    print(response.json())
    print(response.status_code)
