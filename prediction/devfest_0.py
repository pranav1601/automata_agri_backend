from matplotlib import pyplot as plt
import sklearn.preprocessing as pp

def gradient(x,y):
	#converting x,y to float lists
	x = [float(i) for i in x]
	y = [float(i) for i in y]

	N = len(x)
	xy = [x[i]*y[i] for i in range(N)]
	Exy = sum(xy)
	Ex = sum(x)
	Ey = sum(y)
	Ex2 = sum([i**2 for i in x])

	return (N*Exy - Ex*Ey)/(N*Ex2 - (Ex)**2)


def predict(crop, x_list):
	f = open('crop_data/'+crop+'_data.txt', 'r').read().split("\n")
	y = f[0].split(",")
	n = len(f)
	xs = []
	for i in range(1,n-1):
		xs.append(f[i].split(","))
	b = [gradient(xd,y) for xd in xs]
	py = 0
	for i in range(len(b)):
		py = py + b[i]*x_list[i]
	
	return py #predicted value of y


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
		v.append(rf/xs[i])
		if v[i] > v[ind]:
			ind = i

	print(v)
	print(ind)
	return y[ind]


#----PROGRAM EXECUTION STARTS HERE-------
inp = input().strip().split(",")
#il = [float(inp[i]) for i in range(1,len(inp))]
print(enprd(inp[0],float(inp[1])))