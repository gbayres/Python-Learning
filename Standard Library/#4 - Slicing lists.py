def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n] #Let's turn this to a generator

my_list = [2,1,3,4,3,2,3,4,2,3,2,5,3,2]
print(list(chunks(my_list,3)))


#======Short form==========

def slice_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
