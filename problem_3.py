#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600,851,475,143 ?

# it would be simple to brute force check all divisors of the given number
# however it would take about 10 min of running time on a 1GHz processor...
# let's try and be more clever

# a key to this puzzle is to see that you need a prime FACTOR which is a 
# significantly smaller set than largest prime... 

# immediately we see that (n/2 -1) is the largest possible solution
# we can test a set (n/2 -1) - size, for primes then see if they are divisible
# by n (this is assuming that the set of primes will be significantly smaller
# than the set of numbers that divide evenly into n)

# the trick will be figuring out how to 'test' for a prime

# ANOTHER KEY! The "fundamental theorem of arithmatic" states that any number
# is made up of the multiplication of a UNIQUE set of prime numbers

###################### GENERATE THE PRIME LIST ###############################

import time
tic = time.time()   
     
#enter the highest number we want to check to generate our initial list of primes
size = 6900
prime_list = [2]

for n in range(2,size):
    # check for a prime number and compile a prime list
    truth_table =[]    
    for i in prime_list:
        if n%i != 0 and n not in prime_list:
            truth_table.append(0)
        else:
            truth_table.append(1)
#    print 'completed table is', truth_table, n
#    print 'sum table is', sum(truth_table)
    if sum(truth_table) == 0:
        prime_list.append(n)
        
print 'the prime list is ',prime_list

toc = time.time()
print toc-tic, 'sec Elapsed'
# generating a list of primes for the first 5000 numbers takes 20.11 sec

#################### LOOK FOR DIVISORS OF N ##################################

n = 600851475143
prime_in_n = []
a = 1
for i in prime_list:
    if n%i == 0:
        print 'found one!',i
        prime_in_n.append(i)
        a *= i
print 'the largest possible multiple is', n/a

# 6857 is the largest prime factor! this could have been found by choosing 
# size = 1500 and n/a will produce 6857 which will either be a prime (or the
# multiple of two primes greater than 1471... except that it can't be so we 
# could prove that it must be 6875. I'm dense so I just ran the code)
        