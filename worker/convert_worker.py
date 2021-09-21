from pathlib import Path
from worker.worker import Worker
import os


class ConvertWorker(Worker):
    def convert(self):
        for root, dirs, files in os.walk(self.directory, topdown=False):
            for name in files:
                if str(Path(name).suffix) != '.js': continue
                path = root + os.sep + os.sep.join(dirs) + name
                if os.path.exists(path):
                    with open(path, 'r+', encoding='UTF-8') as file:
                        data = file.read()
                        if data.find(self.convertFrom[0]) == -1: continue
                        file.seek(0)
                        file.write(data.replace(self.convertFrom[0], self.convertTo[0]))
                        file.truncate()
        print("done")
