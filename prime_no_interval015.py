#Python Program to Print all Prime Numbers in an Interval

start_num=int(input('Enter a start number: '))
end_num=int(input('Enter a end number: '))

print('Prime numbers between {0} and {1} are'.format(start_num,end_num))
for num in range(start_num,end_num+1):
    if num>1:
        
        for i in range(2,num):
            if num%i==0:
                break
            
        else:
            print(num)