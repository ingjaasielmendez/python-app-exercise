class Item:
    def __init__(self, content, item_name):
        self.name = item_name
        self.content = content

    def get_id(self):
        return self.content['id']
