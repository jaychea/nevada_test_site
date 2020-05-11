num = int(input("Enter a number: "))
for i in range(1, num+1,1):
    x = i
    y = num % i
    if y == 0:
        print(str(x))
        
# % is the modulus operator. If the numbers divided have a remainder, it will print the remainder.
# Therefore, if the remainder of a number is 0, it is a whole number/integer. 
