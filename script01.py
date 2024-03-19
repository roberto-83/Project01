from googlesheet import read_range
from googlesheet import write_range
from webscraper00 import readApiSito
import datetime
import time

timestamp = time.time()
datetime_object = datetime.datetime.fromtimestamp(timestamp)
timestamp1 = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
#val1 = readApiSito("robpol1983@gmail.com")
#print(val1)
#val2 = readApiSito("polegato.ro@gmail.com")
#print(val2)
#val3 = readApiSito("roberto.polegato@libero.it")
#print(val3)

val4 = read_range('Sheet1!A2:G30')
print(val4)
#values=[["1","2"]]
#write_range("Sheet1!E1:F1", values)

#loop su risultato
index = 2 
for x in val4:
  temp = readApiSito(x[1])
  inter = "Sheet1!D"+str(index)+":F"+str(index)
  values=[[temp[0],temp[1],timestamp1]]
  write_range(inter, values)
  print(x[1]+"___"+temp[0]+"___"+temp[1])
  index += 1

