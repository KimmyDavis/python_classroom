def primeCheck(num):
    x = round(num ** 0.5)
    while x > 1:
        if num % x == 0:
            return str(num) + " has a factor of " + str(x)
        x -= 1
    else:
        return str(num) + " is prime!"
print(primeCheck(49))