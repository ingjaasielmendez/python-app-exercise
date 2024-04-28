import requests


def get_todos(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_todos(url="https://jsonplaceholder.typicode.com/todos/")[:3])
