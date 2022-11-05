import re 
from collections import Counter
def reader(filename): #reading file and creating new list 

    regexp = r'.(\d{4}.\d{2}.\d{2}\s\d{2}:\d{2})....\sNOK'
    
    with open(filename) as f:
        log = f.read()

        nok_list = re.findall(regexp, log)

        count(nok_list)    

    return count(nok_list) 
# count number of occurrences
def count(nok_list):
   count = Counter(nok_list)
    
   return count


# convert to readable format 
for key  in reader('log.txt'): 
    print(key, 'NOK ', reader('log.txt')[key])