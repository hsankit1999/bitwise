def set_bit_len(n):             #return no. of set bits
    count=0
    while n:
        n&=n-1
        count+=1
    return count

def only_one_bit_set(n):        #return true if only one bit set
    if n and not(n&(n-1)):
        return True
    else:
        return False

def off_rightmost_bit(n):       #turn off rightmost bit
    return n&(n-1)

def bin(n):                     #print decimal number into binary
    if n>1:
        bin(n//2)
    print(n%2,end="")

def bit_len(n):                 #return length of bit
    length=0
    while n:
        length+=1
        n=n>>1
    return length

def set_bit(n,offset):          #return set bit at given position
    m=1<<offset-1
    return m|n

def clear_bit(n,offset):        #turn off bit at given position
    m=~(1<<offset-1)
    return n&m

def flip_bit(n,offset):         #flip bit at given position
    m=1<<offset-1
    return m^n

    
def isSparse(n):                #return true if there are no adjacent 1's in binary representation
    if((n & 0xAAAAAAAA) and (n & 0x55555555)):
        return False
    else:
        return True

def swap_even_odd(n):           #swap all even and odd bits
    m=n & 0xAAAAAAAA            #A=1010 Even bit
    m=m>>1
    p=n & 0x55555555            #5=0101 Odd bit
    p=p<<1
    return m|p

def modulo_by_pof2(n,d):        #return modulo by power of 2
    if d and not(d&d-1):
        return n&(d-1)
    else:
        return -1


    
