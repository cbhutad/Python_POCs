import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

def patchcall():
    """
        Perform a patch http request from API for free web service of JSONPlaceHolder. Here Patch differs from Put in the way that in case of put we update the entire resource or part of it but we pass the entire exisiting resource as part of request body. In case of patch we specify the part of data to update than entire resource
    """

    response = requests.get(api_url)
    print(response.json())
    dataToPost = {"title": "Melted Icecream"}
    response = requests.patch(api_url,json=dataToPost)
    print(response.json())
    print(response.status_code)