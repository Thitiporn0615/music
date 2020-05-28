
z=[]
n=[]
t=[]
p=[]

fdata = open('d:\\เครื่องดนตรี.txt','r')
data = fdata.read()
a=data.split('.')
sdata = open('d:\\รายการที่เลือก.txt','w')

from datetime import date
now=date.today().strftime('%Y:%m:%d')
sdata.write('วันที่ยืม %s \n' %now)

print('------รายการเครื่องดนตรี-------\nซอ[1]\nระนาด[2]\nขลุ่ย[3]\nกรับ[4]\nฆ้อง[5]\nจะเข้[6]\nขิม[7]\n------แสดงรายการ[s]-------\n')
while True:
    z=input('เลือกรายการ--->')
    n=input('จำนวน--->')
    if z=='1':
        t.append(a[0])
        p.append(n)
    elif z=='2':
        t.append(a[1])
        p.append(n)
    elif z=='3':
        t.append(a[2])
        p.append(n)        
    elif z=='4':
        t.append(a[3])
        p.append(n)
    elif z=='5':
        t.append(a[4])
        p.append(n)
    elif z=='6':
        t.append(a[5])
        p.append(n)
    elif z=='7':
        t.append(a[6])
        p.append(n)
    elif z=='s':break

#line_no = 1
sdata.write('%s%s'%(t,p))
#line_no = line_no + 1

print(t)
print(p)
