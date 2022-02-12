def numbers(array):
    i = 0
    list =[]
    while i<len(array):
        if type(array[i]) == int:
            list.append(array[i])
        i+=1
    print(list)
numbers(array=[1,'a','b',2])
