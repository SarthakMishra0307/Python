import math as m

# ceil= Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__(), which should return an Integral value.
x = 5.34
near_large_int = m.ceil(x)
near_small_int = m.floor(x)
print(near_large_int)



#  COMBINATION (nCr) comb(n, k) : Return the number of ways to choose k items from n items without repetition and without order.
#  GIVES 0 IN PLACE OF AN ERROR WHEN VALUE OF K EXCEEDS THAN THAT OF N
select = m.comb(10,2)
ways = m.perm (10,2)
print(select)

# fabs : Returns absolute value(in same magnitude only)

# gcd(): Returns greatest common divisor the given numbers will have
gcd = m.gcd(24,48,108)
print(gcd)

sum = m.fsum([21,313,16])
print(sum)

# Roundof SquareRoot karke dega
isSquareRoot = m.isqrt(64)
print(isSquareRoot)

print(m.lcm(45,123,78))

# math.prod(iterable, *, start=1)
# Calculate the product of all the elements in the input iterable. The default start value for the product is 1.
print(m.prod([1,2,3,45,6,7]))

print(m.pow(2, 15))


print(m.log10(100))