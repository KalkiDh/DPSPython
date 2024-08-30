lst=[8,6,5,1,3,9,4,2]
l=len(lst)
for i in range(l-1,-1,-1):
    lst.append(lst[i])
    lst.remove(lst[i])
print(lst)