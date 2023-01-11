def calculator(a,b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a/b
    return {'add': add, 'subtract':subtract, 'multiply':multiply, 'divide':divide}

print(calculator(4, 3)['add'])