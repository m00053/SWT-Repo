import re
import sys

def weather(N_LIST):
    ABS_MIN = 0
    N_MIN = 0
    N_SORTED = []
    for N_INDEX in range(len(N_LIST)):
        N_MIN += N_LIST[N_INDEX]
    ABS_MIN = 2*N_MIN+1
    N_MIN = ABS_MIN
    for INDEX_1 in range(len(N_LIST)):
        for INDEX_2 in range(len(N_LIST)):
            if (N_LIST[INDEX_2]<N_MIN and N_LIST[INDEX_2]>0):
                N_MIN = N_LIST[INDEX_2]
        N_SORTED.append(N_MIN)
        N_LIST[N_LIST.index(N_MIN)] = 0
        N_MIN = ABS_MIN
    return N_SORTED

def football(N_LIST):
    ABS_MIN = 0
    N_MIN = 0
    N_SORTED = []
    for N_INDEX in range(len(N_LIST)):
        N_MIN += N_LIST[N_INDEX]
    ABS_MIN = 2*N_MIN+1
    N_MIN = ABS_MIN

    for INDEX_1 in range(len(N_LIST)):
        for INDEX_2 in range(len(N_LIST)):
            if (N_LIST[INDEX_2]<N_MIN and N_LIST[INDEX_2]>0):
                N_MIN = N_LIST[INDEX_2]
        N_SORTED.append(N_MIN)
        N_LIST[N_LIST.index(N_MIN)] = 0
        N_MIN = ABS_MIN
    return N_SORTED

FILENAME_1 = 'C:\\tmp\\weather.dat'
FILENAME_2 = 'C:\\tmp\\football.dat'
FILES = [FILENAME_1,FILENAME_2]
RANGE_LIST = []
DIFF = 0
N_MIN = 0
NUMBERS = ""

N = ""
CHK_INPUT = ""
while CHK_INPUT != "valid":
    print("Welche Liste soll geprueft werden? [0=weather.dat, 1=football.dat, x=abbrechen]")
    N = input()
    if N == 'x':
        sys.exit()
    elif N == '0':
        N = 0
        CHK_INPUT = "valid"
    elif N == '1':
        N = 1
        CHK_INPUT = "valid"
    else:
        print(N)

F = open(FILES[N])
if N == 0:
    for N_INDEX, line in enumerate(F.readlines()):
        if (N_INDEX >= 2 and N_INDEX < 32):
            NUMBERS = line[6:14]
            NUMBERS = re.sub("((?=[^\\.])\D)", " ", NUMBERS)
            SPACING = "    "
            GROUP = NUMBERS.rpartition(SPACING)
            DIFF = abs(int(GROUP[0]) - int(GROUP[2]))
            RANGE_LIST.append(DIFF)
    print("Das Minimum in der Liste ist " + str(weather(RANGE_LIST)[0]))
elif N == 1:
    for N_INDEX, line in enumerate(F.readlines()):
        if (N_INDEX >= 1 and index < 18):
            NUMBERS = line[43:52]
            NUMBERS = re.sub("-", "", NUMBERS)
            SPACING = "    "
            GROUP = NUMBERS.rpartition(SPACING)
            DIFF = abs(int(GROUP[0]) - int(GROUP[2]))
            RANGE_LIST.append(DIFF)
    print("Das Minimum in der Liste ist " + str(football(RANGE_LIST)[0]))
