class Template():

    title = ''
    params = ''

    def __init__(self, title, params):
        self.title = title
        self.params = params

    def generateTemplate(self):
        template = self._generateTag('title', self.title)
        for param in self.params:
            template += self._generateTag('param', param)
        for param in self.params:
            template += self._generateTag('alias', '')
        for param in self.params:
            template += self._generateTag('check', '')
        template += self._generateTag('return', '', lb=False)
        return template

    def _generateTag(self, name, value, lb=True):
        if lb:
            tagLine = str('@' + name + ' ' + value + '\n')
        else:
            tagLine = str('@' + name + ' ' + value)
        return tagLine