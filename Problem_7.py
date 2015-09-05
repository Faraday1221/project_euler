# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


###################### GENERATE THE PRIME LIST ###############################

import time
tic = time.time()   
     
#this is a brute force method of checking for primes based on definitions
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

# we can use the initial list above as a prime "seed" list and begin to 
# and generate a list of combinations of these terms to that are NOT primes
# then we can check the remaining numbers (which should be a very small list)
# and find if these numbers are primes or not