from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

class Phone(Device):
    def connect(self):
        print("Connecting to the phone network...")

class Tablet(Device):
    def connect(self):
        print("Connecting to the tablet network...")

d1 = Phone()
d2 = Tablet()

d1.connect()
d2.connect()