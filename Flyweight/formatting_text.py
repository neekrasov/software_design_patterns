class FormattedText: # Если загрузить большой объём текста, то будет забито много памяти
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)
        
    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True
            
    def __str__(self):
        buffer = []
        for i, c in enumerate(self.plain_text):
            buffer.append(c.upper() if self.caps[i] else c)
        return ''.join(buffer)
    
class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []
        
    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize
            
        def covers(self, position):
            return self.start <= position <= self.end
    
    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        buffer = []
        for i, c in enumerate(self.plain_text):
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            buffer.append(c)
        return ''.join(buffer)
    
    
if __name__ == '__main__':
    ft = FormattedText('This is a brave new world')
    ft.capitalize(10, 15)
    print(ft)
    
    bft = BetterFormattedText('Make America Great Again')
    bft.get_range(0, 4).capitalize = True
    print(bft)