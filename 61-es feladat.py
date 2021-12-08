re = open('adat.txt','r')
line = re.readline()
print(line)
re.close
#Győri Tamás
re = open('adat.txt','r')
line = re.readline()
while line !='':
    line = line.strip()
    print(line)
    line = re.readline()
re.close()

need = []
re = open('igeny.txt','r')
line = re.readline()
line = re.readline()
rn = int(re.readline())
for i in range(rn):
    line = re.readline()
    line = line.strip()
    need.append(line.split())
re.close

re = open('adat.txt','r')
line = re.readline()
while line !='':
    line = line.strip()
    datas = line.split()
    print('%s/%s %s %s/%s =' % \
        datas[0], datas[1],
        datas[4], datas[2],
        datas[3])
    line = re.readline()
re.close()

class Needs():
    pass
need = []
re = open('igeny.txt','r')
line = re.readline()
line = re.readline()
rn = int(re.readline)
for i in range(rn):
    line = re.readline()
    line = re.readline()
    datas = line.split()
    need.append(Needs())
    need[i].h = int(datas[0])
    need[i].min = int(datas[1])
    need[i].sec = int(datas[2])
    need[i].team = int(datas[3])
    need[i].start = int(datas[4])
    need[i].stop = int(datas[5])
re.close()