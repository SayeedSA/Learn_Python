

try:
    with open('G:\9th Semester All Documents\AI\Python Code\data/new.txt') as fobj:
        content=fobj.read()
        print(content)
except Exception as e:
    print("file error",e)
