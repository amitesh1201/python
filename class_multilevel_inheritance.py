#!/usr/local/bin/python

class Base:
    def display(self, result):
        self.result = result
        print "Result: ", self.result


class Addition(Base):
    def addition(self, num1, num2):
        self.sum = int(num1) + int(num2)
        return self.sum


class Substraction(Addition):
    def substraction(self,num1, num2):
        self.minus = 0
        if int(num1) > int(num2):
            self.minus = int (num1) - int(num2)
        else:
            print "Num1 should be greater than num2."

        return self.minus

a1 = Substraction()
result = a1.addition(10, 20)
a1.display(result)
result = a1.substraction(40,50)
a1.display(result)
