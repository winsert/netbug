fp = open('./proxy.csv', 'r')

ps = []

for line in fp.readlines():
    print line
    ps.append(line.strip('\n').decode('utf-8'))

print ps

fp.close()

