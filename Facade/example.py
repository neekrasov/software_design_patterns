class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)
    
    def write(self, text):
        self.buffer += text
    
    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0
    
    def get_char_at(self, index):
        return self.buffer[index + self.offset]
    
    def append_to_buffer(self, text):
        self.buffer.write(text)
    
    def get_char_at_viewport(self, index):
        return self.get_char_at(index)
    
    def __str__(self):
        return ''.join(self.get_line(0, self.buffer.width))
    
    def get_line(self, start, end):
        return [self.get_char_at_viewport(i) for i in range(start, end)]
    
class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]
    
    def write(self, text):
        self.current_viewport.append_to_buffer(text)
    
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)
    
    def get_char_at_viewport(self, index):
        return self.current_viewport.get_char_at_viewport(index)
    
    def __str__(self):
        return str(self.current_viewport)
    
    def get_line(self, start, end):
        return self.current_viewport.get_line(start, end)
    
if __name__ == "__main__":
    c = Console()
    c.write('hello world')
    print(c.get_line(600, 611))