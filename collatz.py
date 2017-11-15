TICKSIZE = 200000

def collatz(x, col):
    if x in col:
        return True
    else:
        if x % 2:
            c = collatz(3 * x + 1, col)
            if c:
                col.add(x)
                return c
        else:
            c = collatz(x // 2, col)
            if c:
                col.add(x)
                return c
    
def CollatzVerifyTo(t):
    col = {4}

    for i in range(1, t):
        if not collatz(i, col):
            print('failed')
        
        if i % TICKSIZE == 0:
            print('.')
            
        if i % (5 * TICKSIZE) == 0:
            print('{} numbers processed'.format(i))
    
    print('Collatz Conjecture verified up to {}'.format(t))

    
if __name__ == '__main__':
    CollatzVerifyTo(200000000)
    
    