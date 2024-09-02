strin=input("Enter string : ")
dictionary={}

for i in strin.split():

    if i in dictionary.keys():
        val=dictionary[i]
        dictionary[i]=val+1
        
    else:
        dictionary[i]=1
        
print(dictionary)
