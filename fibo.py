# Fibonacci numbers module
def fib(n): # wypisuje na standardowe wyjście ciąg Fibonacciego do n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b

def fib2(n): # zwraca ciąg Fibonacciego do n, jako listę
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result