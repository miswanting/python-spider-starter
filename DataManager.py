import json
import os


class DataManager:
    DATA_FILE = 'data.json'

    def __init__(self):
        # self.data = {}
        pass

    def load_data(self, data):
        if self.is_data_exist():
            data.update(self.read_data())
            return data
        else:
            self.write_data(data)
            return data

    def is_data_exist(self):
        return os.path.exists(self.DATA_FILE)

    def read_data(self):
        with open(self.DATA_FILE) as f:
            return json.loads(f.read())

    def write_data(self, data):
        data = json.dumps(data, ensure_ascii=False)
        self.write_file(self.DATA_FILE, data, 'w')

    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def write_file(self, path, data, mode='wb'):
        with open(path, mode) as f:
            f.write(data)

    def update(self):
        self.write_data()
