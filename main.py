# def do_operation(num1,num2,operation):
#     result=operation(num1,num2)
#     print(f'{result=}')
# def plus(num1,num2):
#     return num1+num2
# def minus (num1,num2):
#     return num1-num2
#
# do_operation(10,10,plus)

lst1=['text1','text2','text3']
# lst2=[]
# for i in lst1:
#     lst2.append(i.upper())
#
# # print(lst2)
#
# def to_upper(text):
#     return text.upper()
# lst3=map(to_upper,lst1)
# print(lst3)
# print(list(lst3))
def change_str(text):
    lst=list(text)
    return '-'.join(lst)

# print(list(map(list,lst1)))
# print(list(map(change_str,lst1)))
# print(list(map(str.upper,lst1)))
#
test1=['a','b','c']
test2=['d','e','f']
test3=['g','h','i']
# def plus(a,b,c):
#     return a+b+c
# print(list(map(plus,test1,test2,test3)))

lst5=[]
for i in range(101):
    lst5.append(i)
#
# print(lst5)
def is_even(number):
    if number % 2 ==0:
        return True
# print(list(map(is_even,lst5)))
# print(list(filter(is_even,lst5)))

def not_is_even(number):
    if number % 2 !=0:
        return True
# print(list(map(is_even,lst5)))
# print(list(filter(not_is_even,lst5)))

mixed=['adsf''sadf',4568,'fdsf',5489,True,[1,2,3],12315,'fhgjfg','huerhiwr',True,215616,'asjhdsa']
def is_str(obj):
    return type(obj) is str
# print(list(filter(is_str,mixed)))

print(list(map(lambda text: text.upper(),lst1)))
print(list(map(lambda text: '-'.join(list(text)),lst1)))
print(list(map(lambda a,b,c:a+b+c,test1,test2,test3)))
print(list(filter(lambda num:num%2==0,lst5)))
