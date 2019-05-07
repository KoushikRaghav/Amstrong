def amstrong(num):
	sum = 0
    	temp = num
	while temp > 0:
  		digit = temp % 10
   		sum += digit ** 3
   		temp /= 10
   	print sum    
if __name__ == '__main__':
    num=153
    res=amstrong(num)







