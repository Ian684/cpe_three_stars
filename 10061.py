import math
limit = 2**20 + 1
prime = [0]*limit
prime[0] = prime[1] = 1
for i in range(limit):
	if prime[i]:continue
	for j in range(i , limit , i):
		prime[j] = i
def fac1(aim , l):
	result = [0]*(l+1)
	for i in range(2 , aim+1):
		temp = i
		while temp != 1:
			result[prime[temp]] += 1
			temp //= prime[temp]
	return result
def fac2(aim , l):
	result = [0]*(l+1)
	temp = aim
	while temp != 1:
		result[prime[temp]] += 1
		temp //= prime[temp]
	return result
while True:
	try:
		n , b = map(int, input().split())
		ans2 = 0
		ans1 = 1 << 60
		for i in range(2 , n+1):
			ans2 += math.log(i , b)	
		ans2 = int(ans2) + 1
		l = max(n , b)
		n = fac1(n , l)
		b = fac2(b , l)
		for i in range(l+1):
			if b[i] == 0:continue
			ans1 = min(ans1 , n[i]//b[i])
		print(ans1 , ans2)
	except EOFError:break
