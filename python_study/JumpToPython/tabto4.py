import sys
src = sys.argv[1]
dest = sys.argv[2]

print(src)
print(dest)

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)

f = open(dest, 'w')
f.write(space_content)
f.close()