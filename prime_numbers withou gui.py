#user input
n = int(input("Enter the value of n: "))
# first we"ll crate a list with boolean values (True)
primelist = [True for i in range(n + 1)]

# Prime numbers start from 2
i = 2
# Mark non-prime numbers as False
while i * i <= n:
    if primelist[i] == True:
        for j in range(i * i, n + 1, i):
            primelist[j] = False
    i = i + 1

# Open a file to save the prime numbers
with open("prime_numbers.txt", "w") as file:
    file.write(f"Prime numbers between 2 and {n} are:\n")
    for i in range(2, n + 1):
        if primelist[i] == True:
            file.write(f"{i} ")  # Write primes to the file
            print(i, end=" ")   # Print primes to the console

print("\nPrime numbers have been saved to 'prime_numbers.txt'.")
