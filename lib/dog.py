class Dog:
    def __init__(self) -> None:
        self._name = ''

    def get_name(self):
        print('getting name')
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 2):
            self._name = name
        else:
            print('Name must be a string between 1 and 25 characters.')

    name = property(get_name, set_name)

# Creating an instance of the Dog class
d = Dog()

# Using the setter method to set the name
d.name = 'hello'

# Using the getter method to get the name
print(d.name)
