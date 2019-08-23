'''Dictionary'''

class mydict:
    def __init__(self):
        self.d={}

    def add_entry(self,k,v):
        self.d[k]=v

    def rem_entry(self,k):
        del(self.d[k])

    def search(self,k):
        if k in self.d.keys():
            print('meaning: ',self.d[k])
        else:
            print('word not found')

    def words_with_same_meaning(self,v):
        print('Words with meaning ',v,' : ',end='\t')
        for k in self.d.keys():
            if self.d[k]==v:
                print(k,end='\t')
        print()

    def disp(self):
        words=list(self.d.keys())
        words.sort()
        print('The Dictionary:\nWord : Meaning')
        for w in words:
            print(w,':',self.d[w])

dic=mydict()
while 1:
    ch=int(input('\n1:add entry\n2:search word'
                 '\n3:search words with same meaning\n4:remove entry\n5:'
                 'display all\nEnter choice: '))
    if ch==1:
        w=input('Enter word: ')
        m=input('Enter meaning: ')
        dic.add_entry(w,m)
    elif ch==2:
        w=input('Enter word: ')
        dic.search(w)
    elif ch==3:
        m=input('Enter meaning')
        dic.words_with_same_meaning(m)
    elif ch==4:
        w=input('Enter word: ')
        dic.rem_entry(w)
    elif ch==5:
        dic.disp()
    else:
        exit()
