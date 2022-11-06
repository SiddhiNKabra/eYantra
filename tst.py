from datetime import datetime
# from datetime import timedelta
# import calendar
# import pandas as pd
import pandas as pd


def sendwapp(phno):
    td = datetime.now()
    db = open('test.csv', 'r')
    dl = db.readlines()
    # print(dl)
    print(len(dl))
    for i in range(len(dl)):
        dl[i] = dl[i].split(',')

    for i in range(1,len(dl)):
        tempd = dl[i][3]
        tempd = datetime.strptime(dl[i][3], "%Y-%m-%d")
        print(tempd)
        print(td)
        d = (tempd - td).days + 1
        print(d)
        if(d==1):
            print('rgsrgfwerg')
            #insert wapp and mail func here
        else:
            break

def iinsert(l):

    dt = datetime.strptime(l[3], "%Y-%m-%d")

    db = open("test.csv", 'r')
    dl = db.readlines()
    for i in range(len(dl)):
        dl[i] = dl[i].split(',')


    i = 1
    while(True):
        tempd = datetime.strptime(dl[i][3], "%Y-%m-%d")
        d = -(tempd - dt).days + 1
        print(tempd)
        print(dt)
        print(d)
        if(d>0):
            i+=1
        else:
            bd = open("temp.csv", 'a')
            dl.insert(i,l)
            f = pd.DataFrame(dl)
            print(f)
            l = f.values.tolist()
            print(l)
            for i in l:
                bd.writelines(i)

            # li = ["fsfe","asfaED","AEFAD"]
            # db.writelines(li)
            break

l = ["2022-11-5","sdrgd",1234567890,"2022-11-7","aluofef"]
iinsert(l)
print('sfsae')
# sendwapp(0)
# db = open('test.csv', 'r')
# db = pd.DataFrame(db)
# print(db)

# d1 = "5-11-2022"
# print(d1)
# d1 = datetime.strptime(d1, "%d-%m-%Y")
# print(d1)
# d3 = d1 + timedelta(days=90)
# print(d3)


