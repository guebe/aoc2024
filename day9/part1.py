
line = list(map(list,open(0).read().splitlines()))
line = line[0]
#print(line)

disk = [] # list of blocks with int(fileid) or None if free
freelist = [] # list of indexes where the free blocks are on disk
file_id = 0
for filesz, freesz in zip(line[::2], line[1::2]):
    #print(filesz, freesz)
    for i in range(int(filesz)):
        disk.append(file_id) # append a block with file_id for every files size
    for i in range(int(freesz)):
        freelist.append(len(disk)) # append to the freelist the index of the None blocks - freesz times
        disk.append(None) # append a None block for every free size
    file_id+=1

for i in range(int(line[-1])): # add the last file which has no freeblock afterwards
    disk.append(file_id)

import sys
#print(disk)
#print(freelist)

for pos in reversed(range(len(disk))):
    file_id = disk[pos]
    if (file_id != None):
        #print(f"{file_id} at {pos}")
        if (len(freelist) == 0):
            break # end of freelist
        else:
            freepos = freelist.pop(0) # first free position
            if freepos < pos: # only move them to the front! never back!
                disk[freepos] = file_id
                disk[pos] = None
            else: # otherwise we are finished
                break 

# checksum
chksum = 0
for i, c in enumerate(disk):
    if c != None:
        #print(f"{i} * {int(c)}")
        chksum += int(c) * i
print(chksum)

sys.exit()


