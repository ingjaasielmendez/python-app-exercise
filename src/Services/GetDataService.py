import requests


def get_todos(url):
    """Scrape the page source from the URL"""
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as err:
        print("Error downloading from server", err)


if __name__ == "__main__":
    try:
        print(get_todos(url="https://jsonplaceholder.typicode.com/todos/")[:3])
    except Exception as e:
        print("General Error:", e)
