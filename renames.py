import sys,os
di='2024-02-14'
for a in os.walk(sys.path[0]):
    for b in a[2]:
        if('CHI_NEW/HTMLs'in a[0])or('%s/HTMLs'%di in a[0])or('/ORI/'in a[0]):
            if b[-4:]=='.bak':
                sp='%s/%s'%(a[0],b)
                tp='%s/%s.htm.bak'%(a[0],'.'.join(b.split('.')[:-1]))
                print(sp,'->',tp)
                os.rename(sp,tp)
