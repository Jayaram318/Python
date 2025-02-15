num = 13195

index = 2
start_number = 1
while start_number <= num/2 :
    if num % start_number == 0:
        if start_number % index == 0:
            print(start_number)
            index += 1 
        
            start_number += 1  
