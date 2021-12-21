from datetime import datetime
log = open('log.txt', 'a')

login = input('Enter your login: ')
password = input('Enter your password: ')

if login == 'admin' and password == 'admin':
    print('Success login', datetime.now())
    log.write(str(datetime.now()) + ' Success login\n')
else:
    print('Login failed', datetime.now())
    log.write(str(datetime.now()) + ' Login failed\n')
log.close() 

words = open('words.txt', 'a')
while True:
    word = input('Enter word: ')
    if len(word.split(' ')) > 1: break
    else: words.write(word + '\n') 
    break
words.close()

nums = open('nums.txt', 'a')
sum = 0
while True:
    num = int(input('Enter number: '))
    if -99 <= num <= 99: sum += num   
    else: 
        nums.write(f'{str(sum)}\n')
        break
nums.close()

numbers = open('numbers.txt', 'r')
output = open('output.txt', 'w')
sum = 0
i = 0
for num in numbers:
    sum += int(num)
    i += 1
output.write(str(sum/i))
numbers.close()
output.close()

numbers = open('numbers.txt', 'r')
output = open('output.txt', 'w')
sum = 0
prod = 1
i = 0
for num in numbers:
    sum += int(num)
    prod *= int(num)
    i += 1

output.write('Sum: ' + str(sum) + '\n')
output.write('Prod: ' + str(prod)+ '\n')
output.write('Arith.sum: ' + str(sum/i)+ '\n')
output.write('Arith.prod: ' + str(prod/i)+ '\n')

numbers.close()
output.close()

shop = open('shop.txt', 'r', encoding='utf-8')
list = shop.read().splitlines()

product = ''
for i, line in enumerate(list, 1):
    if i % 2 == 1: product = line
    else: 
       amount = line.split(' ')[0]
       price = line.split(' ')[1]
       print(f'На складе имеется {amount} {product}ов стоимостью ${price}')
shop.close()











shop.close()