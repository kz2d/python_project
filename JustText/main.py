
a=[]
s=[]
with open('DirtyWord.txt') as dr:
    for i in range(1000):
        c=dr.readline()
        a.append(c[0:c.find('[')].strip())
        s.append(c[c.find(']') + 1::].strip())

print(a)
print('как')

with open('englishWord.txt', 'w+') as d:
    while(a):
        d.writelines(a.pop()+'\n')

with open('rushenWord.txt', 'w+') as d:
    while(s):
        d.writelines(s.pop()+'\n')
