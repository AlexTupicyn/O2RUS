file_path = 'text.txt'

razdel53 = []
ID_list = []
Length_Name = []
pgn = []
Name_paragraph = []
poisk = dict()
n = 0
dl = 0
pg = 0

podschet_strok = 0
with open(file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        w = line.split(" ")
        if len(w) > 2:
            if "-71" in w:
                if w[1] == "-71" and ("5.3." in w[2]):
                    n += 1
                    razdel53.append(line_number)
                    dl = n
                if (w[1] == "-71" or w[0] == "-71") and ("5.2." in w[2] or "5.2." in w[1]):
                    dl = 0
            if dl > 0:
                if "DataLength:" in (''.join(map(str, w)).lstrip()):
                    DataLength = (w[4])

                if w[1] == "Parameter" and w[2] == "Group":
                    if w[7] == ')':
                        pgn.append(w[4])
                        ID = (w[6])
                        ID_list.append(ID)
                        ID_list.append(DataLength)
                        pg += 1

                    else:
                        pgn.append(w[4])
                        ID = (w[7])
                        ID_list.append(ID)
                        ID_list.append(DataLength)
                        pg += 1

                if "LengthParameterNameSPN" in (''.join(map(str, w)).lstrip()) and n > 0:
                    podschet_strok = 1

                if podschet_strok == 1:
                    if w[1] == "-71":
                        podschet_strok = 0
                        poisk[pgn[pg - 1]] = []
                        poisk[str(pgn[pg - 1])].append(Name_paragraph)
                        Name_paragraph = []
                        ID_list.append(Length_Name)
                        Length_Name = []

                    if "444)" in w[1]:
                        Name_paragraph[0] = Name_paragraph[0] + " 444)"
                        Name2 = Name + " 444)"
                        Length_Name[Length_Name.index(Name)] = Name2

                    if "-71" in w[2:]:
                        if w[-5] == "-71":
                            Length = (w[2] + " " + w[3])
                            Length_Name.append(Length)
                            war = str(w[-4]) + "  " + (' '.join(map(str, w[4:-7])).lstrip())
                            Name = (' '.join(map(str, w[4:-7])).lstrip())
                            Length_Name.append(Name)
                            Name_paragraph.append(war)

                        elif len(w) > 5 and w[-4] == "-71":
                            Length = (w[2] + " " + w[3])
                            Length_Name.append(Length)
                            war = str(w[-3]) + "  " + (' '.join(map(str, w[4:-5])).lstrip())
                            Name = (' '.join(map(str, w[4:-5])).lstrip())
                            Length_Name.append(Name)
                            Name_paragraph.append(war)

                        else:
                            Length = (w[2] + " " + w[3])
                            Length_Name.append(Length)
                            war = str(w[-5]) + "  " + (' '.join(map(str, w[4:-7])).lstrip())
                            Name = (' '.join(map(str, w[4:-7])).lstrip())
                            Length_Name.append(Name)
                            Name_paragraph.append(war)

print(ID_list)
# print(poisk)
param_5_2 = {}
name = []
nashli = 0
for key, volue in poisk.items():
    for index in range(len(volue[0])):
        name =[]
        line = ''
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if volue[0][index] in line and (len(volue[0][index]) + 7) == len(line):
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
                    sss = str(volue[0][index])
                    name.append(' '.join(map(str, sss.split()[1:])).lstrip())
                    param_5_2 = {"ID": key,
                                 "Name": name,
                                 "Slot_Scaling": Slot_Scaling,
                                 "Slot_Range": Slot_Range,
                                 "SPN": SPN
                                 } #дописать

                    nashli = 0
print(param_5_2)