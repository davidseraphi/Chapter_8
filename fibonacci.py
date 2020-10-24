import time

cache = {}

def fibonnaci(n):
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonnaci(n-1) + fibonnaci(n-2)
    cache[n] = result
    return result

start = time.time()

for i in range(0, 101):
    result = fibonnaci(i)
    print(i, result)

finish = time.time()
duration = finish - start
print('Computed all 100 in', duration, 'seconds')