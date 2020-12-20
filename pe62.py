'''Cubic permutations
  
Problem 62
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

'''
some cube facts - 
 numbers that end(i.e. one's digit) in 3 have a cube that ends in 7 and vice versa
 those that end in 2 will have a cube that ends in 8 and v.v.
 those that end in 0,1,4,5,6,9 will have a cube that ends in that same number
'''
import time
stime = time.time()
def freq(n):
    s = str(n)
    d = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(s)):
        try:
            d[int(s[i])] += 1
        except:
            d[int(s[i])] = 1
    return d

#print('test',freq(12345436767670000089))



def makeCubes(cap):
    results = {}
    results2 = {}
    for i in range(1,cap+1):
        results[i] = i**3
        results2[i**3] = None
    return results, results2

def get_perms(n):
    #pass
    #print('hello')
    #print(n)
    from itertools import permutations
    
    #print(permutations(str(n)))
    return [''.join(p) for p in permutations(str(n))], set(permutations(str(n)))

def is_cube(n):
    if n**(1/3) == int(n**(1/3)):
        return True
    else:
        return False
    
cubevals, cubekeys = makeCubes(10**6)


print('make cubes finished')
mctime = time.time()
print('time {}'.format(mctime-stime))
#l, i = get_perms(1234567890)



def cube_freq():
    print('creating cube freq')
    cube_freq = {}
    for value in cubekeys.keys():
        cube_freq[value] = freq(value)
    print('cube freq finished')
    cftime = time.time()
    print('time {}'.format(cftime-mctime))
    print('checking cube freq')
    for key, value in cube_freq.items():
        count = 0
        breakflag = False
        for k, v in cube_freq.items():
            if k <= key:
                break
            if v == value:
                count += 1
            if count >= 3:
                print(value)
                breakFlag = True
                break
        if breakflag:
            break
    print('done checking cube freq')
cube_freq()
    
def main():

    ########
    print('testing some cubes')
    progress_counter = 0
    for cube in cubekeys.keys():
        #break#this approach sucks
        progress_counter += 1
        if progress_counter % 10000 == 0:
            print('progress:', progress_counter)
        cube_perm_count = list(cube_freq.values()).count(cube_freq[cube])
        if cube_perm_count > 4:
            print(cube)
        

    ttime = time.time()
    print('testing finished',ttime-cftime,'sec')

    
    print('all finished')
    endtime = time.time()
    print('total time {}'.format(endtime-stime))
#main()






