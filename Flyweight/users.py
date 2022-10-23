import random
import string


class User:
    def __init__(self, name):
        self.name = name

class User2:
    strings = []
    
    def __init__(self, name) -> None:
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            self.strings.append(s)
            return len(self.strings) - 1
        self.names = [get_or_add(s) for s in name.split(' ')]
    
    def __str__(self) -> str:
        return ' '.join([self.strings[i] for i in self.names])

def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

if __name__ == '__main__':
    users = []
    first_names  = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]
    
    for first in first_names:
        for last in last_names:
            user = User2(f'{first} {last}')
            users.append(user)
    print(users[0], users[1], users[2])