from matplotlib import pyplot as plt
import sklearn.preprocessing as pp


def enprd(crop, rf):
	f = open('crop_data/'+crop+'_data.txt', 'r').read().split("\n")
	y = f[0].split(",")
	y = [float(q) for q in y]
	n = len(f)
	xs = []
	xs = f[1].split(",")
	xs = [float(q) for q in xs]

	v = []
	v.append(xs[0]/rf)
	ind = 0
	for i in range(1,len(xs)):
		v.append(rf-xs[i])
		if v[i] > v[ind]:
			ind = i

	'''print(v)
	print(ind)
	exit()'''
	if rf >= min(xs) and rf <= max(xs):
		return y[ind]
	else:
		return y[ind]*rf/xs[ind]


#----PROGRAM EXECUTION STARTS HERE-------
inp = input().strip().split(",")
#il = [float(inp[i]) for i in range(1,len(inp))]
print(enprd(inp[0],float(inp[1])))
