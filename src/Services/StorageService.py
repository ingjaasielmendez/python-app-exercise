import csv
from src.Models.ItemClass import Item

storage_status = False
all_ok = False


def storage(items_list, filepath="../../test_storage/"):
    global storage_status
    try:
        for item in items_list:
            item_keys = []
            item_file_name = filepath + item.name + ".csv"
            for key, value in item.content.items():
                item_keys.append(key)
            save(item_file_name, item_keys, item.content)
    except Exception as err:
        print("Error storing data", err)
        storage_status = False
    if storage_status and all_ok:
        print("CSV files created")
    elif storage_status or all_ok:
        print("Not all CSV files were created successfully")
    else:
        print("No CSV file has been created")


def save(item_file_name, item_keys, item_content):
    global storage_status
    global all_ok
    try:
        with open(item_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=item_keys)
            writer.writeheader()
            writer.writerow(item_content)
        storage_status = True
        all_ok = True
    except Exception as err:
        print("Error saving data", err)
        all_ok = False


if __name__ == "__main__":
    content_1 = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    content_2 = {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}
    content_3 = {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}
    item1 = Item(content_1, item_name='test_1')
    item2 = Item(content_2, item_name='test_2')
    item3 = Item(content_3, item_name='test_3')
    items_list_test = [item1, item2, item3]
    storage(items_list_test)
