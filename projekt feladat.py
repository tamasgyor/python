A= set([2,4,6,8,10])
B= set([1,3,5,7,9])
C = A.union(B)      
print(C)

A= set([2,4,6,8,10])
B= set([1,2,3,4,5,6,7,9,10])
C = A.difference(B)
print(C)


A= set([2,4,6,8,10])
B= set([1,3,5,7,9])
A.difference_update(B)
print(A)

A= set([2,4,6,8,10])
B= set([1,2,3,4,5,7,9])
C = A.intersection(B)
print(C)

A= set([2,4,6,8,10])
B= set([1,2,3,4,5,7,9])
A.intersection_update(B)
print(A)

A= set([2,4,6,8,10])
B= set([1,2,3,4,5,7,9])
C = A.isdisjoint(B)
print(C)

A= set([2,4,6,8,10])
B= set([1,3,5,7,9])
C = A.isdisjoint(B)
print(C)


A= set([2,4,6,8,10])
B= set([1,2,3,4,5,7,9])
C = A.issubset(B)
print(C)

A= set([2,4,])
B= set([2,4,])
C = A.issubset(B)
print(C)

