# def numofBits(n):
#     ones=0
#     zeroes=0
    
#     while(n):
#         if(n & 1):
#             ones+=1
#         else:
#             zeroes+=1
#         n=n>>1
        
#     print("Number of ones=",ones, "Number of zeros=",zeroes)
    
# number=int(input("Enter a number:"))
    
# numofBits(number)






def setornot(number,n):
    mask=1
    if (n & mask)==1 or (n & mask)==0:
        if number & (1<<(n-1)):
            print("SET")
        else:
            print("NOT SET")
number=int(input("Enter a number:"))
n=int(input("Enter the position:"))
setornot(number,n)