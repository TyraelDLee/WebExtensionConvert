from pathlib import Path
from worker.worker import Worker
import os
import json

"""
The number in API list:
-1: deprecated
 0: not implemented by this browser
 1: supported
 2: Specific OS only
"""
class CompatibilityWorker(Worker):
    file_name = []
    warning = ''
    error = ''
    api_list = {}

    def __init__(self, args):
        super().__init__(args)
        with open("API_list.json", 'r') as data:
            self.api_list = json.load(data)

    def check(self):
        for root, dirs, files in os.walk(self.directory, topdown=True):
            for name in files:
                try:
                    name.encode('utf-8').decode('ascii')
                except UnicodeDecodeError:
                    self.file_name.append(str(root+os.sep+name).replace(self.directory,""))
                if str(Path(name).suffix) != '.js': continue
                path = root + os.sep + name
                if os.path.exists(path):
                    location = 0
                    for line in open(path, 'r', encoding='UTF-8'):
                        line = line.replace(' ', '').replace('\"', '\'')
                        location += 1
                        if ('extraHeaders' in line or 'extraHeaders' in line) and self.convertTo[1] == 'firefox':
                            self.error += 'ERROR: extraHeaders is not support by firefox\r\n\tFile .'+str(path).replace(self.directory, "") + " line " + str(location) + "\r\n"
                        if 'http://' in line:
                            self.error += 'WARNING: unsafe request found, please consider converting the request to https.\r\n\tFile .'+str(path).replace(self.directory, "") + " line " + str(location) + "\r\n"
                        if self.convertTo[0] in line or self.convertFrom[0] in line:
                            self.compatibility_check(line, str(path).replace(self.directory, ""), str(location))

        if len(self.warning) > 0:
            print(self.warning)
        if len(self.error) > 0:
            print(self.error)
        if len(self.file_name) and self.convertTo[1] == "firefox":
            fileErr = ("WARNING: Non-ASCII file name found. Errors might occur on "+self.convertTo[1]+" by file name. \r\nPlease consider replace Non-ASCII file name.\r\nAt\t")
            for name in self.file_name:
                fileErr += ("."+name + "\r\n\t")
            print(fileErr)

    def compatibility_check(self, data, path, location):
        webType = str(self.convertTo[1])
        for api in list(self.api_list.keys()):
            if "chrome" in self.api_list[api].keys() or "firefox" in self.api_list[api].keys():
                if api + "." in data:
                    self.status_code_all(api=api, webType=webType, path=path, location=location)
            else:
                for method in list(self.api_list[api].keys()):
                    if api+"."+method in data:
                        self.status_code(api, method, webType, path, location)
        pass

    def status_code(self, api, method, webType, path, location):
        if self.api_list[api][method][webType] == -1:
            self.warning += "WARNING: " + self.convertTo[0] + api+"."+method + " API is deprecated!\r\n\tFile ." + path + " line " + location + "\r\n"
        if self.api_list[api][method][webType] == 0:
            self.error += "ERROR: " + api+"."+method + " is not supported by " + webType + "\r\n\tFile ." + path + " line " +location + "\r\n"
        if self.api_list[api][method][webType] == 2:
            self.warning += "WARNING: " + api+"."+method + " API is only available on ChromeOS!\r\n\tFile ." + path + " line " + location + "\r\n"

    def status_code_all(self, api, webType, path, location):
        if self.api_list[api][webType] == -1:
            self.warning += "WARNING: " + self.convertTo[0] + api + " API is deprecated!\r\n\tFile ." + path + " line " + location + "\r\n"
        if self.api_list[api][webType] == 0:
            self.error += "ERROR: " + api + " is not supported by " + webType + "\r\n\tFile ." + path + " line " +location + "\r\n"
        if self.api_list[api][webType] == 2:
            self.warning += "WARNING: " + api + " API is only available on ChromeOS!\r\n\tFile ." + path + " line " + location + "\r\n"
        pass
