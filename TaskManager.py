import collections


class TaskManager:
    def __init__(self):
        self.data = {
            'running': {},
            'channels': {}
        }

    def load_task(self):
        pass

    def save_task(self):
        pass

    def new_task(self, task, channel='default'):
        if channel in self.data['channels']:
            self.data['channels'][channel].append(task)
        else:
            self.data['channels'][channel] = collections.deque([task])

    def get_task(self, channel='default'):
        return self.data['channels'][channel][0]

    def finish_task(self, channel='default'):
        return self.data['channels'][channel].popleft()

    def is_empty(self, channel='default'):
        if not channel in self.data['channels']:
            self.data['channels'][channel] = collections.deque([])
        if len(self.data['channels'][channel]) == 0:
            return True
        else:
            return False

    def set_monitor(self, func):
        pass
