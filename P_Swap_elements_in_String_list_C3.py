# using regex
 
# Initializing list
import re
 
lst = ['Gfg', 'is', 'best', 'for', 'Geeks']
 
# printing original lists
print("The original list is : " + str(lst))
 
# Swap elements in String list
# using regex
res = [re.sub('-', 'e', re.sub('e', 'G', re.sub('G', '-', sub))) for sub in lst]
 
 
# printing result
print("List after performing character swaps : " + str(res))
