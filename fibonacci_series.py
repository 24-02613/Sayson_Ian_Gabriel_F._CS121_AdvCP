number = int(input("Enter the number of terms: "))

firstnum, secondnum = 0, 1

print (f"Fibonacci Series: ", end=" ")

for _ in range(number):
    print(firstnum, end=" ")
    next= firstnum + secondnum
    firstnum = secondnum
    secondnum = next