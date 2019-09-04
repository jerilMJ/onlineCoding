''' Solution to 'Polar Coordinates' under Python in HackerRank '''

import cmath
complex_num = complex(input())

real_part = complex_num.real
imaginary_part = complex_num.imag
phi = cmath.phase(complex(real_part, imaginary_part))

distance = (real_part**2 + imaginary_part**2)**0.5

print(distance)
print(phi)
