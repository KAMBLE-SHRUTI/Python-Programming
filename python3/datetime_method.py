
#datetime method
#frist method
import datetime
print(datetime.datetime.now())

#second method
import datetime as d
print(datetime.datetime.now())

#third method
import datetime as d
x=d.datetime.now()
print(x)

#day,month,year,weekday,month displayed
import datetime as d
x=d.datetime.now()
a=(x.strftime("%d"))            #date
b=(x.strftime("%m"))            #month
c=(x.strftime("%Y"))            #year
d=(x.strftime("%A"))            #weekday
e=(x.strftime("%B"))            #month
print(a,b,c,d,e)

'''
#fourth method
from datetime import datetime
x=datetime.datetime.now()
print(x)
'''



