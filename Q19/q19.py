from itertools import permutations
import time

start = time.perf_counter()

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97]

evens= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

PE=[]
count=0

def solve(equation):
  
    # replacing all the x terms with j 
    # the imaginary part
    s1 = equation.replace('x', 'j')
    
    # shifting the equal sign to start 
    # an opening bracket
    s2 = s1.replace('=', '-(')
    
    # adding the closing bracket to form 
    # a complete expression
    s = s2+')'
    
    # mapping the literal j to the complex j
    z = eval(s, {'j': 1j})
    real, imag = z.real, -z.imag
    
    # if the imaginary part is true return the
    # answer
    if imag:
        return "%f" % (real/imag)
    else:
        if real:
            return "No solution"
        else:
            return "Infinite solutions"


for P in primes:
    for E in evens:
        PE.append([P, E])

for perms in PE:
    P=perms[0]
    E=perms[1]

    equation = f"({P})+(x)*{E} = 1000*{E}+(x)*(-1)*{P}"

    result = solve(equation)

    if float(result).is_integer():
        count = count+1

    

print(count/len(PE))


end = time.perf_counter()
# Convert to milliseconds
elapsed_ms = (end - start) * 1000
print(f"Execution time: {elapsed_ms:.3f} ms")