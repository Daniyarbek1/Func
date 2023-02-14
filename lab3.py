import random
# A = (int(input("Vvedite chislo A:")))
# B = (int(input("Vvedite chislo B:")))

# myliat = list(range(A,B+1))
# print(myliat)

# for i in enumerate(myliat):
#     print(i)

# A = random.randint(0,100)
# B = random.randrange(0,100,2)
# if A < B :
#     mylist = list(range(A,B+1))
#     for i in enumerate(mylist):
#         print(i)

# else :
#     mylist = list(range(B,A-1))
#     for i in enumerate(mylist,-1):
#         print(i)

# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b, -1):
#         print(i)
    
        
n = int(input('Всего карточек:'))
sum = 0
for i in range(1, n + 1):
    sum += i
print('Введите все карточки, помимо потерянное:')
for i in range(n - 1):
    sum -= int(input())
print(f'Потерянная карточка: {sum}')