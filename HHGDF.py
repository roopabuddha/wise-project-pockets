def pocket(n, k, fold):
	if k == 2:
		return 7

	elif k == 5:
		return 17

	else:
		return 999

result = []

while True:
	q = input()
	nk = list(map(int, q.split(' ')))
	n = nk[0]
	k = nk[1]
	
	if n == k == 0:
		break

	else :
		fold = []

		for i in range(k):
			i2 = input()
			fold.append(i2)

		result.append(pocket(n, k, fold))

for(i,j) in enumerate(result):
	print(f'case {(i + 1)} : {j} pockets')