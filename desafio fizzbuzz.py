from time import sleep as sl
from os import system as sy
sy("cls")
print("Bem vindo a minha solução ao: Desafio FizzBuzz")
sl(3)
sy("cls")
sl(1.5)
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    sl(0.5)