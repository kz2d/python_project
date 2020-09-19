
a={}


with open('englishWord1.txt') as dr1:
    with open('englishWord1.txt') as r1:
        with open('englishWord.txt') as dr:
            with open('RushenWord.txt') as r:
                for i in range(1000):
                    c1=dr.readline()
                    c2=r.readline()
                    c3=dr1.readline()
                    c4=r1.readline()
                    #a.append(c[0:c.find('[')].strip(),append(c[c.find(']') + 1::].strip())
                    a[c1]=c2
                    a[c3]=c4


h=[]
s=[]


with open('englishWord11.txt', 'w+') as d:
    with open ( 'rushenWord11.txt' , 'w+' ) as s:
        for i in a.keys():
            d.writelines(i+'\n')
            s.writelines(a[i]+'\n')
# a=set
#
#
#
#
# with open('englishWord.txt', 'w+') as d:
#     while(a):
#         d.writelines(a.pop()+'\n')
#
# with open('rushenWord.txt', 'w+') as d:
#     while(s):
#         d.writelines(s.pop()+'\n')
