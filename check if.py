x = ["a","b","c","d","e","f","g"]
z=["a","b","c","d","e","f","g","h"]

missing=[]


for i in z:
    if i not in x:
        missing.append(i)


print (missing)
