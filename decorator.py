def hashdecorator(func):
    def wrapper():
        return "#"+func()
    return wrapper

@hashdecorator
def message():
    return "PythonIsSimple"
print(message())
