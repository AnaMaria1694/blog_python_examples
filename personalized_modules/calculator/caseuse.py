import calculator

a = 4
b = 3
c = 0
result = calculator.sum(a, b)
print(f"a + b = {result}")
result = calculator.sustraction(a, b)
print(f"a - b = {result}")
result = calculator.multiplication(a, b)
print(f"a * b = {result}")
result = calculator.division(a, b)
if result:
    print(f"a + b = {result}")
result = calculator.division(a, c)