
class Client :
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def whm(self):
        print("Im a client")

class Employee(Client) :
    def __init__(self,name,age,spec):
        super().__init__(name,age)
        self._name = name
        self._age = age
        self._spec = spec
    def whm(self):
        print("Im a employee " + self._spec)
    def work(self):
        print("Im working")

    def getSpec(self):
        return self._spec

jo = Client("Jo",21)

jo.whm()

karl = Employee("Karl",22,"Enginear")

karl.whm()
print(karl.getSpec())