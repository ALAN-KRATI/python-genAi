class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def verify_password(self, password):
        return self.__password == password

u = User("Alice", "secure123")
print(u.verify_password("secure12"))  