file_path = 'text.txt'

razdel53 = []
data = []
id = []
pgn = []
Length = []
Name_paragraph = []
poisk = dict()
n = 0
k = 0
vrem = 0
dl = 0
pg = 0
sum = 0

ttt = 0

ggg = 0
podschet_strok = 0
with open(file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        w = line.split(" ")
        if len(w) > 2:
            if "-71" in w:
                if w[1] == "-71" and ("5.3." in w[2]):
                    n += 1
                    razdel53.append(line_number)
                    vrem = line_number
                    dl = n
                if (w[1] == "-71" or w[0] == "-71") and ("5.2." in w[2] or "5.2." in w[1]):
                    dl = 0
            if dl > 0:
                if "DataLength:" in (''.join(map(str, w)).lstrip()):
                    # print("Data", w[4])
                    data.append(w[4])
                    sum += 1
                if w[1] == "Parameter" and w[2] == "Group":
                    if w[7] == ')':
                        # print("PGN ", w[4], " ID ", w[6])
                        pgn.append(w[4])
                        id.append(w[6])
                        pg += 1

                    else:
                        # print("PGN ", w[4], " ID ", w[7])
                        pgn.append(w[4])
                        id.append(w[7])
                        pg += 1

                if "LengthParameterNameSPN" in (''.join(map(str, w)).lstrip()) and n > 0:
                    podschet_strok = 1
                    # print(w)

                if podschet_strok == 1:
                    ggg += 1
                    # if "444)" in w: print(w)

                    if w[1] == "-71":
                        podschet_strok = 0
                        #                   print(pgn[pg-1], " - ", pg)
                        poisk[pgn[pg - 1]] = []
                        #                   print(poisk)
                        poisk[str(pgn[pg - 1])].append(Name_paragraph)
                        Name_paragraph = []

                    if "444)" in w[1]:
                        Name_paragraph[0] = Name_paragraph[0] + " 444)"
                        # print(Name_paragraph)
                    if "-71" in w[2:]:

                        if w[-5] == "-71":
                            # print(w[2], w[3], " ", w[-4])
                            Length.append(w[2] + " " + w[3])
                            war = str(w[-4]) + "  " + (' '.join(map(str, w[4:-7])).lstrip())
                            # print("000",war)
                            Name_paragraph.append(war)
                            ttt += 1

                        elif len(w) > 5 and w[-4] == "-71":
                            # print(w[2], w[3], " ", w[-5])
                            Length.append(w[2] + " " + w[3])
                            war = str(w[-3]) + "  " + (' '.join(map(str, w[4:-5])).lstrip())
                            # print(war,w, line_number)
                            Name_paragraph.append(war)
                            # print(Length)
                            ttt += 1

                        else:
                            Length.append(w[2] + " " + w[3])
                            war = str(w[-5]) + "  " + (' '.join(map(str, w[4:-7])).lstrip())
                            Name_paragraph.append(war)
                            # print(war)
                            ttt += 1

# print(n, razdel53)

print(n, sum, pg, ggg, k, ttt)
param_5_2 = []
nashli = 0
for key, volue in poisk.items():
    print(key)

    for index in range(len(volue[0])):
        print(volue[0][index], end="\n")
        line = ''
        with open("text.txt", "r", encoding="utf-8") as file:
            for line in file:
                if volue[0][index] in line and (len(volue[0][index]) + 7) == len(line):
                    # print(line)
                    nashli = 1
                if (nashli == 1) and ("Slot Scaling:" in line):
                    if line.split()[-4] == ",":
                        Slot_Scaling = (' '.join(map(str, line.split()[2:-4])).lstrip())
                    elif line.split()[-5] == ",":
                        Slot_Scaling = (' '.join(map(str, line.split()[2:-5])).lstrip())
                    else:
                        Slot_Scaling = (' '.join(map(str, line.split()[2:-3])).lstrip())

                if (nashli == 1) and ("Slot Range:" in line):
                    nomer = line.split().index("Operational")
                    Slot_Range = (' '.join(map(str, line.split()[2:nomer])).lstrip())

                if (nashli == 1) and ("SPN:" in line):
                    SPN = (''.join(map(str, line.split()[1])).lstrip())

                    param_5_2.append(Slot_Scaling)
                    param_5_2.append(Slot_Range)
                    param_5_2.append(SPN)
                    poisk[key][volue[0][index]].append(param_5_2)

                    nashli = 0
print(poisk)