import re
import sys

def weather(list):
  abs_min=0
  min=0
  sorted=[]
  for index in range(len(list)):
    min+=list[index]
  abs_min=2*min+1
  min=abs_min
  for index_1 in range(len(list)):
    for index_2 in range(len(list)):
      if (list[index_2]<min and list[index_2]>0):
        min=list[index_2]
    sorted.append(min)
    list[list.index(min)] = 0
    min = abs_min
  return sorted

def football(list):
  abs_min=0
  min=0
  sorted=[]
  for index in range(len(list)):
    min+=list[index]
  abs_min=2*min+1
  min=abs_min

  for index_1 in range(len(list)):
    for index_2 in range(len(list)):
      if (list[index_2]<min and list[index_2]>0):
        min=list[index_2]
    sorted.append(min)
    list[list.index(min)] = 0
    min = abs_min
  return sorted

filename_1='C:\\tmp\\weather.dat' 
filename_2='C:\\tmp\\football.dat'
files = [filename_1,filename_2]
rangeList=[]
diff = 0
min=0
numbers=""

n = ""
chk_input = "" 
while chk_input != "valid":
  print("Welche Liste soll geprueft werden? [0=weather.dat, 1=football.dat, x=abbrechen]")
  n = input()
  if n=='x':
    sys.exit()
  elif n=='0':
    n = 0
    chk_input="valid"
  elif n=='1':
    n = 1
    chk_input="valid"
  else:
    print(n)

f = open(files[n])
if n==0:
  for index, line in enumerate(f.readlines()):
    if (index >= 2 and index < 32):
      numbers = line[6:14]
      numbers = re.sub("((?=[^\\.])\D)", " ", numbers)
      spacing = "    "
      group = numbers.rpartition(spacing)
      diff = abs(int(group[0]) - int(group[2]))
      rangeList.append(diff)
  print("Das Minimum in der Liste ist " + str(weather(rangeList)[0]))
elif n==1:
  for index, line in enumerate(f.readlines()):
    if (index >= 1 and index < 18):
      numbers = line[43:52]
      numbers = re.sub("-", "", numbers)
      spacing = "    "
      group = numbers.rpartition(spacing)
      diff = abs(int(group[0]) - int(group[2]))
      rangeList.append(diff)
  print("Das Minimum in der Liste ist " + str(football(rangeList)[0]))