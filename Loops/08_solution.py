# Prime number
number = 29
is_prime = True

while number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
    break  

print(is_prime)
