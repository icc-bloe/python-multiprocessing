
class Packet:

    def __init__(self, content):
        self.var1 = 12
        self.var2 = 34
        self._content = content

    def _getContent(self):
        return self._content

    content = property(_getContent)