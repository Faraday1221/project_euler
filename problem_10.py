#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

#Having discovered the Seive in problem 7 we can use that fcn to help with this 
#Problem

import os
os.system("problem_7.py")

x=sieve(int(2e6))
print sum((map(int,x)))