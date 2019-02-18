# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:14:30 2018

@author: abhijeet.singh
"""

#sort the list for send_item
def sort(list,trans,k):
    l = []
    i=0
    for x in list:
        list[i] += trans[i][k]
        i+=1
    for x in list:
        l.append(list.index(min(list)))
        list[list.index(min(list))] = 2*max(list)
    return l

#sends aged or surplus item to a new location
def send_item(left,trans,k):
    left2 = list(left)
    l = sort(left2,trans,k)
    i = 0
    final = []
    for x in left:
        final.append(0)
    sum = 0
    while left[k] != 0 and k != l[i]:
        m = left[l[i+1]]+trans[l[i+1]][k]-left[l[i]]-trans[l[i]][k]
        if left[k]  > m:
            left[k] -= m
            m /= (i+1)
            j = 0
            while j <= i :
                sum += m
                final[l[j]] += m
                left[l[j]] += m
                j+=1
        else:
            m = left[k]/(i+1)
            left[k] = 0
            j = 0
            while j <= i:
                sum += m
                final[l[j]] += m
                left[l[j]] += m
                j+=1
        i+=1
    #printing final transaction
    print ("send %d from warehouse index : %d",sum,k+1)
    i = 0
    for x in final:
        if x > 0:
            print ("received %d at index: %d from index: %d ",x,i+1,k+1)
        i+=1

#Decides which items need to be moved from the warehouse
def priority_warehouse(aged,left):   #the aged are aged in left
    max = 0
    i = 0
    for x in aged:
        if x > max:
            max = x
            k = i
        i+=1
    if max != 0:
        return k
    max = 0
    i = 0
    for x in left:
        if x > max:
            max = x
            k = i
        i+=1
    if max > 0:
        return k

#Draw value from database and compute various arrays of choice
def compute_array(supply,aged,demand,trans):
    i = 0;
    left = []
    for x in supply:
        left.append(x - demand[i])
        aged[i] -= demand[i]
        j = 0
        for y in trans[i]:
            trans[i][j] /= 1000
            j+=1
        i+=1
    return left,aged,trans

#get value from database and run
supply = [200,324,560,178,340]
aged = [72,96,200,58,110]
demand = [134,350,100,75,200]
trans = [[0,1000,2000,3000,4000],[1000,0,2000,3000,4000],[2000,2000,0,3000,4000],[3000,3000,3000,0,4000],[4000,4000,4000,4000,0]]
left,aged,trans = compute_array(supply,aged,demand,trans)
k = priority_warehouse(aged,left)
send_item(left,trans,k)
