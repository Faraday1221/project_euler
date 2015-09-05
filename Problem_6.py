# Problem 6
# sum of squares of numbers 1:100
# square of sum 1:100

x = range(1,101)
y,z=0,0

#sum of squares
for i in x:
    y += i**2
print 'sum of squares is',y

#square of sums
for i in x:
    z += i
print 'the square of sums is',z**2

print 'the difference is', z**2-y


