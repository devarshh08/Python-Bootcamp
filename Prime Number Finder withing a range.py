def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if number < 2:
            continue 
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0: 
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

while True:
    startt = int(input("Start from:"))
    endd = int(input("End till:"))
    print(find_primes(startt, endd))
