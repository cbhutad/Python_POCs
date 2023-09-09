import requests

def getcall():
    """ Performs a get http call to web url provided by API for JsonPlaceHolder """

    # JsonPlaceHolder is free web service that provides fake endpoints and sends back responses"
    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.get(api_url)
    return response.json()

