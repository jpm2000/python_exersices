# Recursividad 

# Un programa se llama así mismo para resolver un problema

# Factorial de un numero y serie de fibonacci


# Factorial 5! = 5*4*3*2*1

# Factorial(n) = n*factorial(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(5))

# Fibonacci 

"""
0 1 1 2 3 5 8 13 21 34...

F(0) = 0
F(n-1) + F (n-2)

"""


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
num = 7

print(fibo(num))


# Calcular de la sumatoria de numeros naturales


'''
Sum(4) = 4+3+2+1

Sum(n) = n + sum(n-1)
'''

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
num_2 = 5

print(sum(num_2))