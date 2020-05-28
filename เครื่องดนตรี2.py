choose=[]#เลือกชนิดเครื่องดนตรี
z=[]#เลือกเครื่องดนตรี
n=[]#จำนวนเครื่องดนตรี
t=[]
p=[]
fdata = open('d:\\เครื่องดนตรีไทย.txt','r')
dataf = fdata.read()
f=dataf.split('.')

kdata = open('d:\\เครื่องดนตรีสากล.txt','r')
datak = kdata.read()
k=datak.split('.')

sdata = open('d:\\รายการที่เลือก.txt','a')

name=input('ชื่อ-สกุล-->')

while True:
    print('---------------------------')
    print('\nเครื่องดนตรีไทย[t]\nเครื่องดนตรีสากล[e]\nแสดงรายการ[s]\n')
    choose=input('เลือกชนิดเครื่องดนตรี->')
    choose=choose.lower()
    if choose=='t':
        print('------รายการเครื่องดนตรีไทย-------\n  ซอ[1]\n  ระนาด[2]\n  ขลุ่ย[3]\n  กรับ[4]\n  ฆ้อง[5]\n  จะเข้[6]\n  ขิม[7]\n  ออก[x]\n')
        while True:
            z=input('เลือกรายการ--->')
            n=input('จำนวน--->')
            if z=='1':
                t=('%s:%s'%(f[0],n))
                p.append(t)
            elif z=='2':
                t=('%s:%s'%(f[1],n))
                p.append(t)
            elif z=='3':
                t=('%s:%s'%(f[2],n))
                p.append(t)        
            elif z=='4':
                t=('%s:%s'%(f[3],n))
                p.append(t)
            elif z=='5':
                t=('%s:%s'%(f[4],n))
                p.append(t)
            elif z=='6':
                t=('%s:%s'%(f[5],n))
                p.append(t)
            elif z=='7':
                t=('%s:%s'%(f[6],n))
                p.append(t)
            elif z=='x' or n=='x':break
    elif choose=='e':
        print('------รายการเครื่องดนตรีสากล-------\n  กีตาร์[1]\n  ไวโอลิน[2]\n  แซ็กโซโฟน[3]\n  ฟลุท[4]\n  ทรัมเป็ท[5]\n  ทูบา[6]\n  กลอง[7]\n  ออก[x]\n')
        while True:
            
            z=input('เลือกรายการ--->')
            n=input('จำนวน--->')
            if z=='1':
                t=('%s:%s'%(k[0],n))
                p.append(t)
            elif z=='2':
                t=('%s:%s'%(k[1],n))
                p.append(t)
            elif z=='3':
                t=('%s:%s'%(k[2],n))
                p.append(t)        
            elif z=='4':
                t=('%s:%s'%(k[3],n))
                p.append(t)
            elif z=='5':
                t=('%s:%s'%(k[4],n))
                p.append(t)
            elif z=='6':
                t=('%s:%s'%(k[5],n))
                p.append(t)
            elif z=='7':
                t=('%s:%s'%(k[6],n))
                p.append(t)
            elif z=='x' or n=='x':break
    elif choose=='s':break
#------------------------วันที่ยืม------------------------------
from datetime import date
now=date.today().strftime('%d/%m/%Y')
#------------------------วันที่คืน------------------------------
day=now.split("/")
d=int(day[0])+5
m=int(day[1])
y=int(day[2])

if m==1 and d>31:
    s=int(d-31)
    d=s
    m=2
elif m==2 and d>28:
    s=int(d-28)
    d=s
    m=3
elif m==3 and d>31:
    s=int(d-31)
    d=s
    m=4
elif m==4 and d>30:
    s=int(d-30)
    d=s
    m=5
elif m==5 and d>31:
    s=int(d-31)
    d=s
    m=6
elif m==6 and d>30:
    s=int(d-30)
    d=s
    m=7
elif m==7 and d>31:
    s=int(d-31)
    d=s
    m=8
elif m==8 and d>31:
    s=int(d-31)
    d=s
    m=9
elif m==9 and d>30:
    s=int(d-30)
    d=s
    m=10
elif m==10 and d>31:
    s=int(d-31)
    d=s
    m=11
elif m==11 and d>30:
    s=int(d-30)
    d=s
    m=12
elif m==12 and d>31:
    s=int(d-31)
    d=s
    m=1
fday=('%d/%d/%d'%(d,m,y))

sdata.write('ชื่อ-สกุล: %s\nวันที่ยืม: %s\nวันที่คืน: %s\n%s\n______________________________________________________________________________________________________\n'%(name,now,fday,p))
#-------------------------แสดงรายการ---------------------------------
print('{0:*<40}'.format(""))
print('ชื่อ-สกุล: %s'%name)
print('วันที่ยืม: %s'%now)
print('วันที่คืน: %s'%fday)
print('{0:-<40}'.format(""))
print('{0:<12}{1:<10}{2:<10}'.format('ลำดับที่','รายการ','จำนวน'))
print('{0:-<40}'.format(""))

count=0
for x in p:
    count+=1
    print(count,end=")       ")
    b=x.split(":")
    print('{0[0]:<13}{0[1]:<6}'.format(b))
print('{0:*<40}'.format(""))
print('--------ขอบคุณค่ะ--------')