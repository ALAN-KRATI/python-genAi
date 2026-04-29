class Machine:
    def start(self):
        print("Machine is starting...")

class Printer(Machine):
    def start(self):
        print("Printer is printing...")

p = Printer()
m = Machine()

m.start()
p.start()