from pathlib import Path
from worker.worker import Worker
import os


class CompatibilityWorker(Worker):
    warning = ''

    def check(self):
        for root, dirs, files in os.walk(self.directory, topdown=False):
            for name in files:
                if str(Path(name).suffix) != '.js': continue
                path = root + os.sep + os.sep.join(dirs) + name
                if os.path.exists(path):
                    with open(path, 'r', encoding='UTF-8') as file:
                        data = file.read()
                        if data.find(self.convertTo) != -1:
                            self.deprecated_check(data, str(path).replace(self.directory, ""))
                        file.seek(0)
        if len(self.warning) > 0:
            print(self.warning)

    def deprecated_check(self, data, path):
        if data.find(self.convertTo+"extension.") != -1:
            self.warning += "WARNING: " + self.convertTo + "extension API is deprecated!\r\n" \
                            "At " + path + " line " +"\r\n"
