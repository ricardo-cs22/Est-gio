def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci_number(number):
    fib_sequence = fibonacci_sequence(number)
    if number in fib_sequence:
        return f"{number} pertence à sequência de Fibonacci."
    else:
        return f"{number} não pertence à sequência de Fibonacci."

numero = 21

resultado = check_fibonacci_number(numero)
print(resultado)