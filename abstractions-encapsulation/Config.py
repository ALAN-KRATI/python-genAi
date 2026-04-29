class Config:
    def __init__(self, version):
        self.__version = version

    def get_version(self):
        return self.__version
    
c = Config("1.0.0")
print(c.get_version()) 