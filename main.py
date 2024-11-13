def numofBits(n):
    ones=0
    zeroes=0
    
    while(n):
        if(n & 1):
            ones+=1
        else:
            zeroes+=1
        n=n>>1
        
    print("Number of ones=",ones, "Number of zeros=",zeroes)
    
number=int(input("Enter a number:"))
    
numofBits(number)