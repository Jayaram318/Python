num1 = 1
num2 = 2

while num1 + num2 < 4000000:

    result = num1 + num2
    num1 = num2
    num2 = result
    
    if result % 2 == 0:
    
      print(result)
    
