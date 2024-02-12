
class Client :
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def whm(self):
        print("Im a client")


jo = Client("Jo",21)

jo.whm()

