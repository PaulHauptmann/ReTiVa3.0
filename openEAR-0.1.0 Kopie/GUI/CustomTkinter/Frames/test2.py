class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class VariableMonitor(Subject):
    def __init__(self):
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.notify()


class SomeClass(Subject):
    
    var1 = VariableMonitor()
    var2 = VariableMonitor()
    var3 = VariableMonitor()

class Observer:
    def update(self, subject):
        print(f'{type(subject).__name__} has been changed')

class AnotherClass:
    def __init__(self):
        self.some_class = SomeClass()
        self.observer = Observer()
        self.some_class.attach(self.observer)

    def change_variable(self, variable_name, new_value):
        setattr(self.some_class, variable_name, new_value)
