#Each new term in the Fibonacci sequence is generated by adding the previous two 
#terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not exceed 
#four million, find the sum of the even-valued terms.

f1 = 0
f2 = 1
fib = 0
ans = []

# this is jon's solution
while fib < 4e6: 
    fib = f1 + f2
    f2 = f1    
    f1 = fib
#    print 'f2 =',f2, 'f1 =',f1, 'fib =',fib
    if f2%2 == 0:
        ans.append(f2)
#        print 'even f2 =',f2, 'sum = ', ans
print sum(ans)      



## this is sonya's solution
#n1 = 0
#n2 = 1
#fib = n1 + n2
#fib_last = n2
#sav_fib = 0
#last_fib = 0
#
#while fib <= 90:
#    sav_fib = fib
#    fib = fib + last_fib
#    if fib > 90:
#        break
#    last_fib = sav_fib
#    print "fib =", fib
    