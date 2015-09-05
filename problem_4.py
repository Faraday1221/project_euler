
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

x,y=999,100
list_pal=[]

for i in range(x,y,-1):
    for n in range(x,y,-1):
        a=i*n
#            print i,n,'mult',a
        if str(a)[0] == str(a)[-1]:
            if str(a)[1] == str(a)[-2]:
                if str(a)[2] == str(a)[-3]:
#                    print 'touchdown we have palindrome', i,'x',n, '=', a
                    list_pal.append(a)

print max(list_pal)