import csv
from src.Models.ItemClass import Item


def storage(items_list, filepath="../../test_storage/"):
    for item in items_list:
        item_keys = []
        item_file_name = filepath + item.name + ".csv"
        for key, value in item.content.items():
            item_keys.append(key)
        save(item_file_name, item_keys, item.content)
    print("Done")


def save(item_file_name, item_keys, item_content):
    with open(item_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=item_keys)
        writer.writeheader()
        writer.writerow(item_content)


if __name__ == "__main__":
    content_1 = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    content_2 = {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}
    content_3 = {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}
    item1 = Item(content_1, item_name='test_1')
    item2 = Item(content_2, item_name='test_2')
    item3 = Item(content_3, item_name='test_3')
    items_list_test = [item1, item2, item3]
    storage(items_list_test)
