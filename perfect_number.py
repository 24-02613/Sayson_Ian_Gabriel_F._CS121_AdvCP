number = int(input("Enter a number: "))
divisor = 0

for i in range (1, number): 
    if number % i == 0:
        divisor += i

if divisor == number:
    print (f"{number} is a perfect number")
else:
    print (f"{number} is not a perfect number.")