# 1. Swap two numbers without a temp variable.

def swap(a,b):
    a,b = b,a
    return a,b
print(swap(2,3))

# 2.  Calculate area of a circle.
import math
def area_circle(r: float) -> float:
    if r <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * r * r
print("area of circle is", area_circle(4))

# 3. Check if a number is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

# 4. Print Fibonacci series up to 10 terms.
def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a, end =" ")
        a, b= b, a+b
        
fib(10)

# 5. Write a function to check prime numbers.
def prime(n):
    if n <= 1 :
        return False    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False        
    return True    
print(prime(7))
print(prime(10))

# 6. Find factorial using a function.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
# 7. : Reverse a list without using reverse().
def rev_list(l1):
    result = l1[::-1]
    return result
    
print(rev_list([10,24,35,14]))

# 8. : Find max and min in a tuple.
def max_min(T1):
    max = min = T1[0]
    for num in T1:
        if num > max:
            max = num
        if num < min:
            min = num            
    return max, min    
print(max_min((10,24,35,14)))

# 9 : Find common elements in two sets.
a = {2,3,5,6}
b = {3,4,2,8,9}
result = a & b
print(result)

# 10 : : Check if a string is a palindrome.
def is_palindrome(str):
    return str == str[::-1]
print(is_palindrome("one"))

# 11 : squares = [i**2 for i in range(1,11)]
print(squares)

#12: Merge two dictionaries.
dict1.update(dict2)
Print(dict1)


