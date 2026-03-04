#skonczone
import matrix as mtx
import transpose as ts
        
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
