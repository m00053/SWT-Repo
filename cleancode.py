#importiere regular_expression fuer regulaere ausdruecke
import re
#importiere sys fuer Konsole
import sys

#definiere sort_by_minimum fuer beide Listen
def sort_by_minimum(list):
  absolute_minimum=0
  list_minimum=0
  #leere Ziel-Liste 'sorted'
  list_sorted= [None] * len(list)
  #bestimme abs_min = 2*summe(liste)+1
  for index in range(len(list)):
    list_minimum+=list[index]
  absolute_minimum=2*list_minimum+1
  list_minimum=absolute_minimum
  #n mal Liste durchgehen fuer das naechste Minimum
  for n in range(len(list)):
    for list_index in range(len(list)):
      if (list[list_index]<list_minimum and list[list_index]>0):
        list_minimum=list[list_index]
    list_sorted[n] = list_minimum
    #loesche dort Eintrag weil in sorted uebertragen
    list[list.index(list_minimum)] = 0
    list_minimum = absolute_minimum
  return list_sorted[0]

filename_1='C:\\tmp\\weather.dat' 
filename_2='C:\\tmp\\football.dat'

#Liste fuer Rohdaten aus f
rangeList=[]

#Initialisierung Variablen fuer Sortieren
diff = 0
min=0
numbers=""

#Variablen-Gruppe 'weather'
weather_range_min=6
weather_range_max=14
weather_list_min=2
weather_list_max=32
weather_sub_1="((?=[^\\.])\D)"
weather_sub_2=" "

#Variablen-Gruppe 'football'
football_range_min=43
football_range_max=52
football_list_min=1
football_list_max=18
football_sub_1="-"
football_sub_2=""

ranges_min = [weather_range_min,football_range_min]
ranges_max = [weather_range_max,football_range_max]
filenames = [filename_1,filename_2]
lists_min = [weather_list_min,football_list_min]
lists_max = [weather_list_max,football_list_max]
sub_1 = [weather_sub_1,football_sub_1]
sub_2 = [weather_sub_2,football_sub_2]

#Kontroll-Variable fuer Listen-Modus
mode = 0
check_input = ""
while check_input != "valid":
  print("Welche Liste soll geprueft werden? [w=weather.dat, f=football.dat, x=abbrechen]")
  check_input = input()
  if check_input=='x':
    sys.exit()
  elif check_input=='w':
    mode = 0
    check_input="valid"
  elif check_input=='f':
    mode = 1
    check_input="valid"
  else:
    print(check_input)
f = open(filenames[mode])
for index, line in enumerate(f.readlines()):
  if (index >= lists_min[mode] and index < lists_max[mode]):
    numbers = line[ranges_min[mode]:ranges_max[mode]]
    numbers = re.sub(sub_1[mode], sub_2[mode], numbers)
    spacing = "    "
    group = numbers.rpartition(spacing)
    diff = abs(int(group[0]) - int(group[2]))
    rangeList.append(diff)

print("Das Minimum in der Liste ist " + str(sort_by_minimum(rangeList)))