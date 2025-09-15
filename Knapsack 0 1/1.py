def knap(capacity,value,weight,n):
    if n == 0 or capacity == 0:
        return 0
    pick = 0
    
    if weight[n-1]<=capacity:
        pick = value[n-1] + knap(capacity - weight[n-1],value,weight,n-1)
        notpick = knap(capacity,value,weight,n-1)
        return max(pick,notpick)
    else:
        return knap(capacity,value,weight,n-1)

weight = [10,20,30]
value = [100,2000,30000]
capacity = 40

print("total value in bag:",knap(capacity,value,weight,len(value)))