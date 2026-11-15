a=int(input('kindly enter a number: '))
b=int(input('kindly enter a number: '))
try:
    result=a/b
    result1=a+b
    print(result,result1)
except ValueError as ve:
    print('kindly add an valid value',ve)
except ZeroDivisionError as ve:
    print('kindly dont add 0',ve)
except NameError as ex:
    print('variable not defined',ex)        


