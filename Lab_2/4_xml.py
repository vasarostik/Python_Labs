#w1 = set(input('word #1: '))
#w2 = set(input('word #2: '))
 
#print('{} common letters'.format(len(w1.intersection(w2))))


with open('a.txt','r') as infile:
	lst = []
	for line in infile:
		words = line.split()
		for word in words:
			for word1 in words:
				print('{}'.format(len(word[-3:].intersection(word1[-3:]))))

