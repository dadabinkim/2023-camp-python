# n=int(input())
# if n%3==0:
#     print(f'{n}은 3의 배수입니다')
# else:
#     print(f'{n}은 3의 배수가 아닙니다')
# for i in range(1, 11, 1):
#     print(i, end=' ')
# u=int(input())
# if u%2==0:
#     print('짝수입니다')
# else:
#     print('홀수입니다')
# r=int(input())
# t=int(input())
# y=int(input())
# o=r
# if r<t:
#     o=t
# if y>o:
#     o=y
# print(o)

# for i in range(6, 0, -1):
#     for j in range(i):
#         print('*',end='')
#     print()
# for i in range(-1, 8, 2):
#     for k in range(8-(i//2)+1):
#         print(' ', end='')
#     for j in range(i):
#         print('*',end='')
#     print()
# a=int(input())
# b=int(input())
# for i in range(a, b+1):
#     if i%2!=0:
#         print(i)
# y=int(input())
# for i in range(1, y+1):
#     if i==3 or i==6 or i==9:
#         print('-', end='')
#     else:
#         print(i, end='')
a=int(input())
b=int(input())
c=str(input())
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="/":
    print(a/b)
elif c=="*":
    print(a*b)
