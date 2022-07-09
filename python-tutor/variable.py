print("Hello")
print("World")

"""
    Data type
    1. int
    2. float
    3. String
    4. bool (Boolean) => True, False
    5. list
    6. tuple
    7. dict
    
    Operator
    1. number (int, float)
        - +
        - - 
        - *
        - /
        - %
        - **
        - //
    2. String
        - +
        - *
    3. boolean
        - and
        - or
        - not
"""

x = 8
y = 10.5
name = "Aungkoon"
boo = False

result = x / 5
result2 = (((10+2)-8)*4)/6
result2 = 10+2-8*4/6
result3 = boo and True

print(type(y))
print(name*4)
print(result)
print(result2)
print(result3)

print("my result is "+str(result2)+" "+str(result)) # 6.6666 => "6.6666"
print(f"my result is {result2:.2f} {result:.4f}") # f-string
