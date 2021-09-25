#compiler time errror(syntax error)
#runtime error(a=5,b=0)here no output we get.
#logical error(5+5=55)is logical error

a=5
b=0
try:
    print('resource open ')
    print(a/b)
except Exception as e:
    print('you cant execute this line',e)
finally:
    print('resource close')
    print('sayeed')