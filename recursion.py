#sum of n natural numbers,
n=int(input("Enter the number : "))
def sum_of_natural_numbers(n):
    if n==0:
        return 0
    return sum_of_natural_numbers(n-1) + n
result = sum_of_natural_numbers(n)
print(f"The sum of first {n} natural numbers is: {result}")
   
    