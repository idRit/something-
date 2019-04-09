import math

def prime_factors(n):

    list_of_primes = []

    while n % 2 == 0: 
        list_of_primes.append(2)
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            list_of_primes.append(i) 
            n = n / i 

    if n > 2: 
        list_of_primes.append(i)

    return list_of_primes

file_get = open("get.txt")

n = int(file_get.read())
list_of_primes = prime_factors(n)

file_set = open("set.txt", "w+")
file_set.write(str(list_of_primes))
file_set.close()

file_get.close()