"""Implement the Fractional Knapsack problem for
given weights and values."""

def knap(capacity,weight,values):
    items = [(values[i]/weight[i] , values[i],weight[i]) for i in range(len(values))]
    items.sort(reverse=True)

    bag = 0
    for r,v,w in items:
        if capacity >= w:
            capacity -= w
            bag += v
        else:
            bag += r * capacity
            break
    return bag

weight = [10,20,30]
values = [1000,300,30]
capacity = 50

print("max value in bag :",knap(capacity,weight,values))

      