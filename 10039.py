def cal(s , time , start , end):
	global all
	dp = [[-1]*len(all) for _ in range(1441)]
	t1 , t2 , de = s[start]
	for j in range(len(t1)):
		if t1[j] < time:continue
		dp[t2[j]][all.index(de[j])] = max(t1[j] , dp[t2[j]][all.index(de[j])])
	for x in range(1441):
		for y in range(len(all)):
			if dp[x][y] == -1:continue
			if all[y] == end:continue
			t1 , t2 , de = s[all[y]]
			for i in range(len(t1)):
				if t1[i] < x:continue
				dp[t2[i]][all.index(de[i])] = max(dp[t2[i]][all.index(de[i])] , dp[x][y])
	for x in range(1441):
		if dp[x][all.index(end)] != -1:
			return [dp[x][all.index(end)] , x]
	return "No connection"
num = int(input())
for i in range(num):
	print(f"Scenario {i+1}")
	station = int(input())
	stations = {}
	all = []
	for j in range(station):
		temp = input()
		all.append(temp)
		stations[temp] = [[],[],[]]
	q = int(input())
	result = []
	for j in range(q):
		p = int(input())
		temp = input().split()
		temp[0] = int(temp[0][0:2])*60 + int(temp[0][2:4])
		for k in range(p-1):
			temp1 = temp[:]
			stations[temp1[1]][0].append(temp1[0])
			temp = input().split()
			temp[0] = int(temp[0][0:2])*60 + int(temp[0][2:4])
			stations[temp1[1]][1].append(temp[0])
			stations[temp1[1]][2].append(temp[1])
			
	time = input()
	time = int(time[0:2])*60 + int(time[2:4])
	start = input()
	end = input()
	ans = cal(stations , time , start , end)
	if ans == "No connection":
		print(ans)
	else:
		temp1 , temp2 = str(ans[0]//60) , str(ans[0]%60)
		temp3 , temp4 = str(ans[1]//60)  ,str(ans[1]%60)
		temp1 = '0'*(2-len(temp1)) + temp1
		temp2 = '0'*(2-len(temp2)) + temp2
		temp3 = '0'*(2-len(temp3)) + temp3
		temp4 = '0'*(2-len(temp4)) + temp4
		print(f"Departure {temp1}{temp2} {start}")
		print(f"Arrival   {temp3}{temp4} {end}")
	if i != num - 1:print()
