number =  3128
max_number = 4000

while True:
    n = 1
    d = number//2
    while True:
        n = n + 1
        # This line check if `number` (the one we want to check whether it's
        # prime) is perfectly divisible by `n` (a possible divisor that could
        # prove that `number` is not prime)"""
        if (number // n) == (number / n):
                # if `number` is not prime, we should say so and break out of the
                # inner while loop that's iterating through possible divisors
                print(f"{number} is not prime (it's divisible by {n})")
                # update the `maybe_prime` variable, so when we exit the inner
                # `while` loop we know that we found a divisor.
                break
        elif n > d:
            print(f"{number} is prime")
            break
    number += 1
    if number > max_number:
         break
    
    
