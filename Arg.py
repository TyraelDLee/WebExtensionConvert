import os
import sys

class Args:
    args = {}
    convert = ''
    direction = ''
    error = ''
    supportType = "cfs"
    usage = """usage: python convert.py <path> convertType
    
    covertType are:
    c-f    Convert chrome API to firefox API
    f-c    Convert firefox API to chrome API
    """

    def parse(self) -> None:
        if len(sys.argv) < 3:
            self.error = self.usage
            return

        if not os.path.exists(sys.argv[1]) and not os.path.exists(sys.argv[2]):
            self.error = "Source directory not found."
            return

        if os.path.exists(sys.argv[1]) and "-" not in sys.argv[2]:
            self.error = "convertType error.\r\n"+self.usage
            return
        else:
            convertType = sys.argv[2].split("-")
            if convertType[0] not in self.supportType or convertType[1] not in self.supportType:
                self.error = "convertType error.\r\n"+self.usage
                return
            self.args['dir'] = sys.argv[1]
            self.args['convertFrom'] = self.convert_type(convertType[0])
            self.args['convertTo'] = self.convert_type(convertType[1])

    def convert_type(self, type):
        rtype = ""
        if type == 'c':
            rtype = "chrome."
        if type == "f":
            rtype = "browser."
        return rtype
