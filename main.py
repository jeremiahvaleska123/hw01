# hw01
python作业
for i in range(9,-1,-1):
    for k in range(9-i+1,0,-1):
        print("\t",end=' ')
    for j in range(1,i+1,1):
            print("%dx%d=%-3d"%(j,i,i*j),end=' ')
    print()        
