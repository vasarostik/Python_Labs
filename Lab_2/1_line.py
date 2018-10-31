file = open('my.txt','r')
ros=[]
for line in file:
	ros.append(line)

print(ros)
file.close()
