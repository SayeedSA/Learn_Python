#unchangable
import sys
tuple=[2,1,3,4,5,6,7,8,9]
list=[2,1,3,4,5,6,7,8,9]
print(tuple.remove(tuple[1]))
print('tuple', sys.getsizeof(tuple))
print('list', sys.getsizeof(list))
del tuple #full akebare delete korte hoi
print(tuple)
