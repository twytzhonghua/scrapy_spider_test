a = 52
times = 5
per_time = a /times

for i in range (0, times):
	begin =  i * per_time
	stop =  (i + 1)* per_time - 1
	print("begint = %d   " %  begin )
	print('stop = %d \n' % stop )
	
begin = (i + 1)* per_time
stop = a

print("begint = %d   " %  begin )
print('stop = %d \n' % stop )