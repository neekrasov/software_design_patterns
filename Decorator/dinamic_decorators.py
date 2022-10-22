class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def write(self, text):
        print(f'Writing {text} to {self.file.name}')
        self.file.write(text)
        
    def __iter__(self):
        return self.file.__iter__()
    
    def __next__(self):
        return next(self.file)

    def __getattr__(self, item):
        return getattr(self.file, item)
    
    def __setattr__(self, key, value) -> None:
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.file, key, value)
    
    def __delattr__(self, item) -> None:
        if item == 'file':
            raise AttributeError("Can't delete file")
        else:
            delattr(self.file, item)
            
if __name__ == "__main__":
    with open('Decorator/files/some_file.txt', 'w') as f:
        f = FileWithLogging(f)
        f.write('hello world')