import numpy as np
def is_prime(x):
    if x ==1:
        return False
    for i in range(int(np.sqrt(x))):
        if x%(i+1)==0 and (i+1)!=1:
            return False
    return True

def primes_up_to_x(x):
    primes = []
    for i in range(int(x)):
        if is_prime(i+1):
            primes.append(i+1)
    return primes

def which_divisors(x,primes,divisors):
    for i in range(int(x)):
        div = i+1
        if div!=1 and x%div == 0 and (div in primes):
            if x == 1:
                if div in divisors:
                    divisors[div]+=1
                else:
                    divisors[div]=1
                return divisors
            else:
                if div in divisors:
                    divisors[div]+=1
                else:
                    divisors[div]=1
                return which_divisors(int(x/div),primes,divisors)

def find_divisors(x):
    primes = primes_up_to_x(x)
    div = {}
    which_divisors(x, primes, div)
    return div
  
    
arr = np.arange(1,21,1)
dictionary = {}

for i in arr:
    div = find_divisors(i)
    for j in div:
        if j in dictionary:
            dictionary[j] = max(div[j],dictionary[j])
        else:
            dictionary[j] = div[j]
result = 1
for i in dictionary:
    result*=i**dictionary[i]
print(result)