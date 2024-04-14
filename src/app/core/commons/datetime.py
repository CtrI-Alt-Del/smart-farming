class Datetime:
    def __init__(self,value):
        self.value = value
        
    def get_value(self):
        return self.value.strftime("%d-%m-%Y %H:%M:%S")