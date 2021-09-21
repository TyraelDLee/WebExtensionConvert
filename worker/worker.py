class Worker:
    directory = None
    convertFrom = None
    convertTo = None

    def __init__(self, args):
        self.directory = args['dir']
        self.convertFrom = args['convertFrom']
        self.convertTo = args['convertTo']