from src.Models.ItemClass import Item


items_list = []


def classify(web_response, identifier='id', date='22_02_2022_'):
    try:
        for content in web_response:
            item_name = date + str(content[identifier])
            create_object(content, item_name)
        return items_list
    except Exception as err:
        print("Error processing data", err)


def create_object(content, item_name):
    item = Item(content, item_name)
    items_list.append(item)
    return


if __name__ == "__main__":
    web_response_test = [
        {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False},
        {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False},
        {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}
    ]
    classify(web_response_test)
    for i in items_list:
        print(i.content)
        print(i.name)
