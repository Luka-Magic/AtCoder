mod = 10**9+7
 
n = int(input())
 
print((10**n%mod-2*(9**n%mod)+8**n%mod)%mod)