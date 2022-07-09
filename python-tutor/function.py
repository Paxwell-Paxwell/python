def printHello():
    for i in range(5):
        print("Hello")

def sum(num1: int = 0, num2: int = 0): # parameters
    result = num1+num2 # scope of variable
    return result, "Hello"
    #print(result)

x = lambda a : a * 3

printHello() # call function

print("----------------")

printHello()
sumValue, text = sum(num2=10, num1=50) # arguments
print(sumValue)
print(text)

resultX = x(10)
print(resultX)
