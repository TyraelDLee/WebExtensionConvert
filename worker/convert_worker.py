from pathlib import Path
import os


class ConvertWorker:
    directory = None
    convertFrom = None
    convertTo = None

    def __init__(self, args):
        self.directory = args['dir']
        self.convertFrom = args['convertFrom']
        self.convertTo = args['convertTo']

    def convert(self):
        for root, dirs, files in os.walk(self.directory, topdown=False):
            for name in files:
                if str(Path(name).suffix) != '.js': continue
                path = root + os.sep + os.sep.join(dirs) + name
                if os.path.exists(path):
                    with open(path, 'r+', encoding='UTF-8') as file:
                        data = file.read()
                        if data.find(self.convertFrom) == -1: continue

                        file.seek(0)
                        file.write(data.replace(self.convertFrom, self.convertTo))
                        file.truncate()
        print("done")
