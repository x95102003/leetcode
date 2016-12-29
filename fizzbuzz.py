# -*- coding: utf-8 -*- 

def fizzBuzz(n):
    '''
    origin version
    result = []
    for i in xrange(1, n+1):
        ans = ''
        if not i % 3:
            ans += 'Fizz'
        if not i % 5:
            ans += 'Buzz'
        if i % 3 and i % 5:
            ans = str(i)
        result.append(ans)
    return result
    '''
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in xrange(1, n+1)]

print fizzBuzz(15)
            
            

