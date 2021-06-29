123123
123123
123123
def my_zip(x1, x2):
	length = min(len(x1), len(x2))
	for i in range(length):
		yield(x1[i], x2[i])

x1 = [1, 2, 3, 4, 5]
names = ('John', 'James', "Jack")

for res in my_zip(names, x1):
	print(res)

