import tkinter as tk
from tkinter import messagebox

# main application window 
root = tk.Tk()
root.title("Prime Number Finder")
root.geometry("400x300")

def find_primes():
    try:
        # user input 
        n = int(entry.get())
        if n < 2:
            messagebox.showerror("error", " enter a number greater than or equal to 2.")
            return
        
        # creating a list with all the values as true
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        #sieve of Eratosthenes algorithm
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        #extract the prime numbers from the list
        primes = [str(i) for i in range(2, n + 1) if is_prime[i]]
        prime_text = " ".join(primes)
        
        #saving prime numbers to a text file
        with open("prime_numbers.txt", "w") as file:
            file.write(f"Prime numbers between 2 and {n} are:\n")
            file.write(prime_text)
        
        #display in the GUI
        output_label.config(text=prime_text)
        messagebox.showinfo("Success", "Prime numbers have been saved to 'prime_numbers.txt'.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# user interface 
label = tk.Label(root, text="Enter a number:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Find Primes", command=find_primes)
button.pack(pady=5)

output_label = tk.Label(root, text="", wraplength=350, justify="left")
output_label.pack(pady=10)

# run the application
root.mainloop()
