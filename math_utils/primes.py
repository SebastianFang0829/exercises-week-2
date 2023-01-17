from math import sqrt

def isprime(n):
    """If n is 1, then directly output Flase. 
    Otherwise, check if the number is zero modulo any of the intergers 
    less than its square root. 
    False if it is zero and return True if none of zero is returned"""
    if n == 1:
        return False 
    else:
        for i in range(1,int(sqrt(n))):
            if n % (i+1) ==0:
                return False
        return True
