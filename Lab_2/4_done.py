import xml.etree.cElementTree as ET
import re

root = ET.Element("root")
doc = ET.SubElement(root, "doc")
words = []
endings = []

def get_endings(array, line):
    result = []
    for index in range(len(array)):
        
        ending_value = re.findall(r'\w\w\w$', array[index])
        if len(array[index]) > 2:
    
            result.extend([{'ending': ending_value[0], 'data': ({'word': array[index], 'word_position': index+1, 'line': line})}])
    return result

with open('my.txt', 'r') as file:
    arr = file.readlines()

    for i in range(len(arr)):
        mapping = [(';', ''), (':', ''), (',', ''), ("'s", ''), ('.', ''), ('\n', '')]
        for k, v in mapping:
            arr[i] = arr[i].replace(k, v).lower()
        words.append(arr[i].split(' '))

    for i in range(len(words)):
        endings.extend(get_endings(words[i], i+1))
       
    for i in range(len(endings)):
        mass=tuple()
        for j in range(len(endings)):
            if endings[j]["ending"] == endings[i]["ending"] and endings[j]["ending"] !='':
                mass+=({"word":endings[j]["data"]["word"],"pos":endings[j]["data"]["word_position"],"line":endings[j]["data"]["line"]},)
                if j>i+1:
                    endings[j]["ending"]=''
        if mass:
            print(mass)
            ET.SubElement(doc, "word ", name=str(endings[i]["ending"])).text = "Length: "+str(len(mass))+str(mass)

tree = ET.ElementTree(root)
tree.write("c.xml")
