import xml.etree.cElementTree as ET
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
lst = []
l = 1

with open('a.txt','r',encoding='utf8', errors='ignore') as infile:
	lst = []
	text = infile.read()
	lst1 = list(text.split())
	newlst1=[]

	for word in lst1:
		word = word.replace(",","")
		word = word.replace(";","")
		word = word.replace(".","")
		newlst1.append(word)
	
 #if j[-1]=='.' or j[-1]==',' or j[-1]==';':
 #				j=j[:len(i)-1]
	for i in newlst1:
		k=0
		for j in newlst1:
			
			if i == j: k+=1

		if i not in lst:
			
			ET.SubElement(doc, "field"+str(l), name=i).text = str(k)
			lst.append(i)
			l+=1     
	lst.sort()
	print(lst)

tree = ET.ElementTree(root)
tree.write("c.xml")
