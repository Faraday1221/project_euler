# 2520 is the smallest number that can be divided by each of the numbers 1:10
# What is the smallest positive number that is evenly divisible (divisible with
# no remainder) by all of the digits 1:20

# using the concept that all numbers are "built" by primes then we can
# investigate the sum of all the prime numbers, then check if that term
# is divisible by all terms 1:20

# we can check this for 1:10 where the primes are (1,2,3,5,7)
# 1*2*3*5*7 = 210, then checking to see if this is evenly divisble we see that
# it does not work for 4,8,9. All of these numbers can be decomposed into the
# sum of primes i.e. 2*2, 2*4, 3*3. We can add this to the current total
# 1*(2*(2*2))*(3*3)*5*7 = 2520


primes=(2,3,5,7,11,13,17,19)
x = 1
#find the sum of all primes < 20
for i in primes:
    x *= i
print x

# added in 3 and 8 (2*2*2) after performing the  analysis below
#x=x*3*8

#check if this term is evenly divisible by 1:20
for i in range(1,21):
    if x%i == 0:
        print 'working as intended ,',i
    else:
        print 'fucked ,',i

# 4, 8, 9, 12, 16, 18, 20 are not divisible
# if the above is correct we could solve this by finding the prime factors
# in the above numbers

# breaking these terms into their prime factors
# 2*2, 2*2*2, 3*3, 3*(2*2), (2*2)*(2*2), (2*3*3), (2*2*5)
# removing overlaps from the prime set i.e. (2,3,5,7,11,13,17,19)
# 2*2*2=8, 3 (note all other terms are already found in the prime set)
# thus the new prime set is (2,2,2,2,3,3,5,7,11,13,17,19) which is also
# the prime factors of the number we are looking to find... thus multiplying them
# together provides the solution

# 3, 8 these are the missing multiples based on the numbers above

# to generalize this we would need to find the set all prime factors of an
# individual number to we want to divide by (e.g. 1:20)
# then remove overlaps between between the sets (of numbers we want to divide by)
# the remaining values would make up the final set of multiples to generate
# the smallest evenly divisible number

