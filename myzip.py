def my_zip(x1, x2):
	length = min(len(x1), len(x2))
	for i in range(length):
		yield(x1[i], x2[i])

x1 = [1, 2, 3, 4, 5]
names = ('John', 'James', "Jack")

for res in my_zip(names, x1):
	print(res)


//another example

def short_seq_range(*args):
    return range(min(map(len, args)))


def Task4():
    a = 'asdfgh'
    b = (10, 20, 30, 40)
    c = ((a[i], b[i])
    for i in short_seq_range(a, b) )

    for item in c:
        print(item)

Task4()