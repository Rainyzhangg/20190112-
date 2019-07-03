#113.428002,22.673163,﻿爱国工业区二路/爱国工业区六巷(路口)
pi = np.pi
a = 6378245.0
ee = 0.00669342162296594323
def transformLat(x,y):
	ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y+ 0.2 * abs(x)**0.5
	ret += (20.0 * np.sin(6.0 * x * pi) + 20.0 * np.sin(2.0 * x * pi)) * 2.0 / 3.0
	ret += (20.0 * np.sin(y * pi) + 40.0 * np.sin(y / 3.0 * pi)) * 2.0 / 3.0
	ret += (160.0 * np.sin(y / 12.0 * pi) + 320 * np.sin(y * pi / 30.0)) * 2.0 / 3.0
	return ret

def transformLon(x,y):
	ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1* np.sqrt(abs(x))
	ret += (20.0 * np.sin(6.0 * x * pi) + 20.0 * np.sin(2.0 * x * pi)) * 2.0 / 3.0
	ret += (20.0 * np.sin(x * pi) + 40.0 * np.sin(x / 3.0 * pi)) * 2.0 / 3.0
	ret += (150.0 * np.sin(x / 12.0 * pi) + 300.0 * np.sin(x / 30.0* pi)) * 2.0 / 3.0
	return ret
	
def transform(lat,lon):
	dLat = transformLat(lon - 105.0, lat - 35.0)
	dLon = transformLon(lon - 105.0, lat - 35.0)
	radLat = lat / 180.0 * pi
	magic = np.sin(radLat)
	magic = 1 - ee * magic * magic
	sqrtMagic = np.sqrt(magic)
	dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * pi)
	dLon = (dLon * 180.0) / (a / sqrtMagic * np.cos(radLat) * pi)
	mgLat = lat + dLat
	mgLon = lon + dLon
	return mgLat,mgLon
	
def gcj02To84():
	data = np.array([[113.428002,22.673163]])
	res = []
	for i in range(1,data.shape[0]):
		c = transform(float(data[i,0]),float(data[i,1]))
		res.append([c[0],c[1]])
	return res
a = gcj02To84()
print(a)
