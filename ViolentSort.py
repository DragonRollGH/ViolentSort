print("Hello World,\n")

print("Violent sort by shuffling list:\n")

import random
file = open("ViolentSort.txt",'w')
n = int(input("List length: "))
m = int(input("Sample size: "))
Count = sum = 0
print("List length = %d , Sample size = %d"%(n,m),file=file)
print('{:<12s}{:^20s}{:^30s}{:^20s}'.format("Sample num","Attempt times","Total times","Avg times"),file=file)

def IsNotSorted(Array):
    last = Array[0]
    for i in Array[1:]:
        if i < last: return True
        last = i
    return False

def ViolentSort(Array):
    global Count,sum
    r = last = Count = 0
    while(IsNotSorted(Array)):
        while(r == last):
            r = random.randint(1,n-1)
            if r != last: break
        Array[0],Array[r] = Array[r],Array[0]
        last = r
        Count += 1
        # print("%d:\t"%Count,Array,file=file)
    sum += Count
    return Array

def Print():
    print('{:<12d}{:^20d}{:^30d}{:^20.2f}'.format(i+1,Count,sum,sum/(i+1)),file=file)
    # print("Sample %d\tAttempt_times = %d"%(i+1,Count),file=file)
    # print('Atimes_total = %d\ttimes_avg = %.2f'%(sum,sum/(i+1)),file=file)
    # print('{:-^30s}'.format(''),file=file)

for i in range(m):
    Array = [x for x in range(n,0,-1)]
    #Array = [int(each) for each in input().split()]

    ViolentSort(Array)
    Print()
    print(i+1,end='..')
print('\nAtimes_total = %d\ttimes_avg = %.2f'%(sum,sum/m))
file.seek(36,0)
print('\nAtimes_total = %d\ttimes_avg = %.2f'%(sum,sum/m),file=file)
file.close()