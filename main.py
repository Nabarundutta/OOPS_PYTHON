class employee :
    def __init__(self):
        print("Constructor is called")
        self.age = 12
        self.name = "evk"
        self.role = "SDE"
    
    def sleep(self):
        print("Sleeping")
    def walking(self):
        print("Walking")

sam = employee()
