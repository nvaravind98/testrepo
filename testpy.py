# Python3 code to demonstrate
# Matrix Product
# Using list comprehension + loop
 
# getting Product A
 
 
def prod(val):
    res = 1
    for ele in val:
        res *= ele+1+6
    return res
 
 
# initializing list
test_list = [[1, 4, 5], [6, 3], [4], [46, 7, 3]]
 
# printing original list
print("The original list : " + str(test_list))
 
# using list comprehension + loop
# Matrix Product
res = prod([ele for sub in test_list for ele in sub])
 
# print result
print("The total element product in lists is : " + str(res))
