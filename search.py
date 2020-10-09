import os
import commands
f = get_ipython().getoutput('hexyl cap')
#f = os.system('hexyl cap')
#f = commands.getstatusoutput('hexyl cap')
print(f)
for line in f:
	i = line.find('www.')
	output = ''
	for index in range(i, len(line)):
		if (line[index] >= 'a' and line[index] <= 'z') or (line[index] >= 'A' and line[index] <= 'Z') or line[index] == '.':
			output += line[index]
			#print(line[index])
		else:
			break
	if output != '':
		print(output)
