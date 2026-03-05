# FIND MAXIMUM NO. >>>>>>

# arr=[12,78,87,56,7]
# maximum= arr[0]

# for num in arr:
#     if num > maximum:
#         maximum = num
# print("maximum no. : ",maximum)



 #EVEN & ODD FIND  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# arr=[1,2,3,4,5,6,7]

# even=0
# odd=0

# for num in arr:
#     if num % 2 ==0:
#         even += 1
#     else:
#         odd+=1
# print("EVEN No. :",even)
# print("ODD No. :",odd)




# SUM OF ALL ELEMEMTS >>>>>>>>>>>>>>>>>>>>

# arr = [5,9,20,600]
# total=0
# for num in arr:
#     total += num 
# print("Sum:",total)






#Linear search      >>>>>>>>>>>>>>>>>>>>>>>>

arr= [10,20,30,40,50]
# target=30  it's show Element Found
target = 80  #Not found

found = False 
for num in arr:
    if num ==target:
        found =True
        break
if found:
    print("Element Found")
else:
    print("Not Founded")







