from datetime import datetime
d= input("Enter date in string: ") # Jul 14 2001
d_obj= datetime.strptime(d,'%b %d %Y')
print(d_obj)