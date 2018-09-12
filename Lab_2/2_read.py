file = open('a_eng.txt','r',encoding='utf8', errors='ignore')
b1 = open('b1.txt','w')
b2 = open('b2.txt','w')

ros=[]
for line in file:
  ros.append(line)
print(ros)

for i in range(0,len(ros),2):
	b1.write(ros[i].lower())

for i in range(1,len(ros)-1,2):
	b2.write(ros[i].upper())

file.close()
b1.close()
b2.close()
