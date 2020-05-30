#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

'''
name =input("Enter file:")
handle = open(name)
count = dict()

for line in handle:
    line.rstrip()
    if not line.startswith('From '): continue
    word = line.split()

    counts=word[5].split(':')
    #print(counts)
    count[counts[0]]=count.get(counts[0],0)+1
lst=list()
for k,v in count.items():
    lst.append((k,v))
lst=sorted(lst)
for k,v in lst:
    print(k,v)  '''
