#skonczone
import matrix as mtx
import transpose as ts
import chio
        
m1 = mtx.matrix(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

m2 = mtx.matrix(
[ [3, 1],
  [2, 1],
  [1, 0]])

print(ts.transpose(m1))

print(m1 + mtx.matrix((2,3), 1))

print(m1 * m2)


mat1 = mtx.matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

] )

deter1 = chio.chio(mat1)

print(deter1)

mat2 = mtx.matrix( [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ] )

deter2 = chio.chio(mat2)
print(deter2)

mat3 = mtx.matrix([
     [0 , 0 , 0 , 0 , 0],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

deter3 = chio.chio(mat3)
print(deter3)

mat4 = mtx.matrix( [
     [0 , 1 , 1 , 2 , 3],
     [0 , 2 , 1 , 7 , 3],
     [0 , 1 , 2 , 4 , 7],
     [0 , 1 , 0 , 7 , 0],
     [0 , 4 , 7 , 2 , 2]
    ])

deter4 = chio.chio(mat4)
print(deter4)