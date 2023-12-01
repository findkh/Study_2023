# 85. XML에서 엘리먼트와 콘텐츠를 읽으려면?
from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
for parent in tree.iter():
    for child in parent:
        print(child.text)