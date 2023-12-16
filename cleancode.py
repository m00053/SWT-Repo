def cleancode():
    #importiere regular_expression fuer regulaere ausdruecke
    import re
    #importiere sys fuer Konsole
    import sys

    #definiere sort_by_MINIMUM fuer beide Listen
    def sort_by_MINIMUM(N_LIST):
        ABSOLUTE_MINIMUM=0
        LIST_MINIMUM=0
        #leere Ziel-Liste 'SORTED'
        LIST_SORTED= [None] * len(N_LIST)
        #bestimme abs_MIN = 2*summe(Liste)+1
        for N_INDEX in range(len(N_LIST)):
            LIST_MINIMUM+=N_LIST[N_INDEX]
        ABSOLUTE_MINIMUM=2*LIST_MINIMUM+1
        LIST_MINIMUM=ABSOLUTE_MINIMUM
        #n mal Liste durchgehen fuer das naechste MINIMUM
        for n in range(len(N_LIST)):
            for LIST_INDEX in range(len(N_LIST)):
                if (N_LIST[LIST_INDEX]<LIST_MINIMUM and N_LIST[LIST_INDEX]>0):
                    LIST_MINIMUM=N_LIST[LIST_INDEX]
            LIST_SORTED[n] = LIST_MINIMUM
            #loesche dort Eintrag weil in SORTED uebertragen
            N_LIST[N_LIST.index(LIST_MINIMUM)] = 0
            LIST_MINIMUM = ABSOLUTE_MINIMUM
        return LIST_SORTED[0]

    FILENAME_1='C:\\tmp\\weather.dat'
    FILENAME_2='C:\\tmp\\football.dat'

    #Liste fuer Rohdaten aus f
    RANGE_LIST=[]

    #Initialisierung Variablen fuer Sortieren
    DIFF = 0
    N_MIN=0
    NUMBERS=""

    #Variablen-Gruppe 'weather'
    WEATHER_RANGE_MIN=6
    WEATHER_RANGE_MAX=14
    WEATHER_LIST_MIN=2
    WEATHER_LIST_MAX=32
    WEATHER_SUB_1="((?=[^\\.])\D)"
    WEATHER_SUB_2=" "

    #Variablen-Gruppe 'football'
    FOOTBALL_RANGE_MIN=43
    FOOTBALL_RANGE_MAX=52
    FOOTBALL_LIST_MIN=1
    FOOTBALL_LIST_MAX=18
    FOOTBALL_SUB_1="-"
    FOOTBALL_SUB_2=""

    RANGES_MIN = [WEATHER_RANGE_MIN,FOOTBALL_RANGE_MIN]
    RANGES_MAX = [WEATHER_RANGE_MAX,FOOTBALL_RANGE_MAX]
    FILENAMES = [FILENAME_1,FILENAME_2]
    LISTS_MIN = [WEATHER_LIST_MIN,FOOTBALL_LIST_MIN]
    LISTS_MAX = [WEATHER_LIST_MAX,FOOTBALL_LIST_MAX]
    SUB_1 = [WEATHER_SUB_1,FOOTBALL_SUB_1]
    SUB_2 = [WEATHER_SUB_2,FOOTBALL_SUB_2]

    #Kontroll-Variable fuer Listen-Modus
    MODE = 0
    CHECK_INPUT = ""
    while CHECK_INPUT != "valid":
        print("Welche Liste soll geprueft werden? [w=weather.dat, f=football.dat, x=abbrechen]")
        CHECK_INPUT = input()
        if CHECK_INPUT=='x':
            sys.exit()
        elif CHECK_INPUT=='w':
            MODE = 0
            CHECK_INPUT="valid"
        elif CHECK_INPUT=='f':
            MODE = 1
            CHECK_INPUT="valid"
        else:
            print(CHECK_INPUT)
    F = open(FILENAMES[MODE])
    for N_INDEX, line in enumerate(f.readlines()):
        if (N_INDEX >= LISTS_MIN[MODE] and N_INDEX < LISTS_MAX[MODE]):
            NUMBERS = line[RANGES_MIN[MODE]:RANGES_MAX[MODE]]
            NUMBERS = re.sub(SUB_1[MODE], SUB_2[MODE], NUMBERS)
            spacing = "    "
            group = NUMBERS.rpartition(spacing)
            DIFF = abs(int(group[0]) - int(group[2]))
            RANGE_LIST.append(DIFF)

    print("Das Minimum in der Liste ist " + str(sort_by_MINIMUM(RANGE_LIST)))
