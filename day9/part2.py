
line = list(map(list,open(0).read().splitlines()))
line = line[0]
#print(line)

disk = [] # list of blocks with int(fileid) or None if free
file = [] # list of files with (idx(disk), length)
file_id = 0
for filesz, freesz in zip(line[::2], line[1::2]):
    #print(filesz, freesz)
    file.append((len(disk), int(filesz)))
    for i in range(int(filesz)):
        disk.append(file_id) # append a block with file_id for every files size
    for i in range(int(freesz)):
        disk.append(None) # append a None block for every free size
    file_id+=1

file.append((len(disk), int(line[-1])))
for i in range(int(line[-1])): # add the last file which has no freeblock afterwards
    disk.append(file_id)

def dbg(disk):
    for block in disk:
        if block is None:
            print('.', end='')
        else:
            print(str(block%10), end='')
    print()

import sys
#dbg(disk)
#print(file)

def find_free(filelen):
    for i in range(len(disk)-filelen):
        if disk[i] is None:
            if all(x is None for x in disk[i:i+filelen]):
                return i
    return None

for filepos, filelen in reversed(file):
    fileid = disk[filepos]
    #print(f"{filepos}: found {fileid=}*{filelen}")
    freepos = find_free(filelen)
    if freepos is not None and freepos < filepos:
        #print(f"free {freepos}")
        for i in range(filelen):
            disk[filepos+i] = None
            disk[freepos+i] = fileid

# checksum
chksum = 0
for i, c in enumerate(disk):
    if c != None:
        #print(f"{i} * {int(c)}")
        chksum += int(c) * i
print(chksum)

sys.exit()


