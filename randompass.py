import random

Upper = 'ABCDEF'
Lower = 'abcdef'
num = 1234567890
sym = "!@#$%^&*()}_+=/?><\]{|"

passw = Upper + Lower + str(num) + sym


def gen():
    password = "".join(random.sample(passw, k=20))
    print(password)

gen()