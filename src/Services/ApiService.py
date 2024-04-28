from sys import stderr
import datetime
from src.Services.GetDataService import get_todos
from src.Services.ClassifyService import classify
from src.Services.StorageService import storage


URL = "https://jsonplaceholder.typicode.com/todos/"
IDENTIFIER = "id"
DATE = datetime.datetime.now().strftime("%Y_%m_%d_")
FILEPATH = "storage/"


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)

        # TODO: follow README.md instructions
        try:
            web_response = get_todos(URL)
            if web_response:
                items_list = classify(web_response, identifier=IDENTIFIER, date=DATE)
                storage(items_list, filepath=FILEPATH)
            else:
                raise Exception("No data")
        except Exception as e:
            print("General Error:", e)
