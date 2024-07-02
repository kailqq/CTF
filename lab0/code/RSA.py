

def ext_gcd(a, b):   
    if b == 0:          
        return 1, 0, a     
    else:         
        x, y, gcd = ext_gcd(b, a % b)         
        x, y = y, (x - (a // b) * y)          
        return x, y, gcd
p = 0x848cc7edca3d2feef44961881e358cbe924df5bc0f1e7178089ad6dc23fa1eec7b0f1a8c6932b870dd53faf35b22f35c8a7a0d130f69e53a91d0330c0af2c5ab
q = 0xa0ac7bcd3b1e826fdbd1ee907e592c163dea4a1a94eb03fd4d3ce58c2362100ec20d96ad858f1a21e8c38e1978d27cd3ab833ee344d8618065c003d8ffd0b1cb
n = p * q
e = 0x10001
d,k,_=ext_gcd(e,(p-1)*(q-1))
c = 0x39f68bd43d1433e4fcbbe8fc0063661c97639324d63e67dedb6f4ed4501268571f128858b2f97ee7ce0407f24320a922787adf4d0233514934bbd7e81e4b4d07b423949c85ae3cc172ea5bcded917b5f67f18c2c6cd1b2dd98d7db941697ececdfc90507893579081f7e3d5ddeb9145a715abc20c4a938d32131013966bea539
m=pow(c,d,n)
print(int.to_bytes(m, (m.bit_length() + 7) // 8, 'big'))

