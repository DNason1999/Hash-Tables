def expensive_seq(x, y, z, cache=None):
    if cache is None:
        cache = {}

    if x <= 0:
        return y + z
    else:
        if x >  0: 
            # first term in cache (x-1,y+1,z)
            if ((x-1,y+1,z) not in cache):
                cache[(x-1,y+1,z)] = expensive_seq(x-1,y+1,z, cache)
            # second term in cache (x-2,y+2,z*2)
            if ((x-2,y+2,z*2) not in cache):
                cache[(x-2,y+2,z*2)] = expensive_seq(x-2,y+2,z*2, cache)
            # third term in cache (x-3,y+3,z*3) 
            if ((x-3,y+3,z*3) not in cache):
                cache[(x-3,y+3,z*3)] = expensive_seq(x-3,y+3,z*3, cache)

            # get terms from cache
            r1 = cache[(x-1,y+1,z)]
            r2 = cache[(x-2,y+2,z*2)]
            r3 = cache[(x-3,y+3,z*3)]
            return r1 + r2 + r3

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
