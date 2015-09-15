# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


#http://stackoverflow.com/questions/19345627/python-prime-numbers-sieve-of-eratosthenes
def sieve(n):
    "Return all primes <= n."
    #this section creates the initial range from 2 to n+1 
    #(since 2 is the first prime & n+1 ensures we will see primes <=n)
    np1 = n + 1
    s = range(np1) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    
    #this has a lot going on with a little code
    #first it evalutes from two to the sqrt of n (this is because the multiples
    #of each digit are removed based on the implementation so using the sqrt is more
    #efficient)
    #then if the limited range appears in the overall set created above
    #all values > i^2 and multiples of i (here implemented as step size i) are zeroed out
    #then the zeros are filtered out of the range that has been operated on 
    for i in xrange(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
            #print s, 'this is when True' #this shows the zeros from filtering above
    return filter(None, s)


#the solution to the 10001 th prime is then
x=seive(2000000)
print x[10000]








######################## JB ATTEMPT 1 #########################################
#this is the basis for what I imagined would be a good implementation to solve
#the problem, it is a start towards the Sieve of Eratosthenese 
#(which I was previously unaware of)
#after some difficulty I turned to google which led me to the Sieve


#stepping through what is a recursive algorithm we see the following
#this should provide the insight to write a formula

#limit=100
#prime_list=[2]
#all_set=range(1,limit,prime_list[-1])
#prime_list.append(all_set[1])
#print all_set, 'all list'
#print prime_list, 'prime list'
#
#remove_set=range(1,limit,prime_list[-1])
#print remove_set, 'remove set'
#
#all_set=list(set(all_set).difference(remove_set))
#print all_set, 'the new set of the difference'
#
#prime_list.append(all_set[1])
#print prime_list, 'the new prime list'
