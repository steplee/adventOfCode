import re, sys
lines = [l.strip() for l in sys.stdin.readlines()]

a,b = '210-=', (2,1,0,-1,-2)
forward = {k:v for k,v in zip(a,b)}
backward = {v:k for k,v in zip(b,a)}

acc = 0
for l in lines:
    y = 0
    for p,m in enumerate(l[::-1]):
        y += (5**p) * forward[m]
    # print(y)
    acc += y

z = acc
coeffs = [None]*11
print(z)


# naive bruteforce cannot work with more than say 14 digits.
# But a beam search, taking the best two choices at each digit
# worked for the final answer.
# The beam search looks for the best fitting two/five digits at each position.

P = 24
# P = 10
def dp(q, p=0):

    beam=[]
    for k,v in backward.items():
        qq = q - (5**(P-1-p)) * v

        if qq == 0: return k
        if abs(qq) > abs(q*2): continue

        beam.append((qq,k,v))

    beam = sorted(beam, key=lambda x:abs(x[0]))

    if p < P:
        for qq,k,v in beam[:2]:
            res = dp(qq, p+1)
            if res is not None: return k + res


    return None


# z = 4890
# coeffs = dp(0)
coeffs = dp(z)
print(coeffs)
