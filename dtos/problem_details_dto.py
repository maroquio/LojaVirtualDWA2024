class ProblemDetailsDto:
    def __init__(self, input, msg, type, loc = None):
        self.input = input
        self.msg = msg
        self.type = type
        self.loc = loc

    def to_dict(self):
        return self.__dict__