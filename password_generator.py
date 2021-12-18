import random
low = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER = '0123456789'
symbol = '!@#$*_-.;'
all = low + up + NUMBER + symbol
size = 9
senha = ''.join(random.sample(all, size))
print(f'A senha que você gerou é: {senha}')