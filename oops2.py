class Calculator :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2

calculator = Calculator(94,10)
data = calculator.add()
print(data)
data = calculator.subtract()
print(data)
data = calculator.multiply()
print(data)
data = calculator.divide()
print(data)


