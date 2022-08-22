f1 = open('file1.txt','w')
f1.write("Hello there!\n")
f1.write('Second line!')

content = """

Awesome content which is being written


= by adithya
"""

f1.write(content)
f1.close()