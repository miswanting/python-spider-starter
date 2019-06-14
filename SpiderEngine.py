import DataManager
import NetManager
import TaskManager
import ThreadManager


class Engine:
    def __init__(self):
        pass

    def config(self):
        pass

    def init(self):
        self.data = DataManager.DataManager()
        self.task = TaskManager.TaskManager()
        self.net = NetManager.NetManager()
        self.thread = ThreadManager.ThreadManager()

    # def load_data(self, data):
    #     self.data.data = data
    #     self.data.load_data()

    # def save_data(self):
    #     self.data.write_data()
    def load_data(self, data):
        return self.data.load_data(data)

    def save_data(self, data):
        self.data.write_data(data)

    def mkdir(self, path):
        self.data.mkdir(path)

    def get(self, url, data=None, encoding='utf-8'):
        return self.net.get(url, data, encoding)

    def post(self, url, data=None, encoding='utf-8'):
        return self.net.post(url, data, encoding)

    def save(self, path, data, mode="wb"):
        self.data.write_file(path, data, mode)

    def load_task(self):
        return self.task.load_task()

    def save_task(self):
        return self.task.save_task()

    def new_task(self, task, channel='default'):
        return self.task.new_task(task, channel)

    def get_task(self, channel='default'):
        return self.task.get_task(channel)

    def finish_task(self, channel='default'):
        return self.task.finish_task(channel)

    def task_is_empty(self, channel='default'):
        return self.task.is_empty(channel)

    def set_mission(self, func, num=1):
        pass


class Project:
    pass


class Mission:
    pass


class Task:
    pass
