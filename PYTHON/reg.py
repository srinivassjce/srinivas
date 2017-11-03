import fileinput
import re
 
for line in fileinput.input():
    line = re.sub('foo','bar', line.rstrip())
    print(line)
