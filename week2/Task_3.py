def even(tuple):

    new_tuple=()

    for i in tuple:
        if i%2==0:
            new_tuple=new_tuple+(i,)
        else:
            pass

    print(new_tuple)

numbers=(1,2,3,4,5,6,7,8,9,10,11)

even(numbers)
