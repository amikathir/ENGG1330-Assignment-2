# Amaresh Kathiresan ENGG1330 Assignment 2 Level 3 UID: 3035962556
island = []
tsuen_wan = []
east_rail = []
kwun_tong = []
tuen_ma = []
station_DB = {1: island, 2: tsuen_wan, 3: east_rail, 4: kwun_tong, 5: tuen_ma}
found_list = []
interchange = []
output_list = []
unique_station_list = []


def format_input(name_input):
    name_input = name_input.lower()
    if name_input == "hku":
        result = "HKU"
    else:
        word_list = name_input.split()
        for i in range(len(word_list)):
            word = word_list[i]
            capital_word = word[0].upper() + word[1:]
            word_list[i] = capital_word
        result = " ".join(word_list)
    return result


def build_database():
    with open("Island Line.txt", "rt") as file:
        for line in file:
            line = line.strip()
            island.append(line)
    with open("Tsuen Wan Line.txt", "rt") as file:
        for line in file:
            line = line.strip()
            tsuen_wan.append(line)
    with open("East Rail Line.txt", "rt") as file:
        for line in file:
            line = line.strip()
            east_rail.append(line)
    with open("Kwun Tong Line.txt", "rt") as file:
        for line in file:
            line = line.strip()
            kwun_tong.append(line)
    with open("Tuen Ma Line.txt", "rt") as file:
        for line in file:
            line = line.strip()
            tuen_ma.append(line)


def make_interchange_list():
    count = 0
    for i in range(1, 5):
        check_line = station_DB.get(i)
        for item in check_line:
            if item not in unique_station_list:
                unique_station_list.append(item)
    for item1 in unique_station_list:
        if item1 in island:
            count += 1
        if item1 in tsuen_wan:
            count += 1
        if item1 in east_rail:
            count += 1
        if item1 in kwun_tong:
            count += 1
        if item1 in tuen_ma:
            count += 1
        if count >= 2:
            interchange.append(item1)
        count = 0


def find_station(name):
    if name in island:
        found_list.append(1)
    if name in tsuen_wan:
        found_list.append(2)
    if name in east_rail:
        found_list.append(3)
    if name in kwun_tong:
        found_list.append(4)
    if name in tuen_ma:
        found_list.append(5)


def build_output_line(check_list):
    for item in check_list:
        if item == 1:
            output_list.append("Island Line: ")
        elif item == 2:
            output_list.append("Tsuen Wan Line: ")
        elif item == 3:
            output_list.append("East Rail Line: ")
        elif item == 4:
            output_list.append("Kwun Tong Line: ")
        elif item == 5:
            output_list.append("Tuen Ma Line: ")


def build_output_station(check_list, interchange_list):
    temp_list = []
    count = 0
    for item in check_list:
        station_list = station_DB.get(item)
        for item2 in station_list:
            for item3 in interchange_list:
                if item2 == item3:
                    temp_list.append(item2)
        temp_list.sort()
        starting_string = output_list[count]
        attach_string = ", ".join(temp_list)
        output_list[count] = starting_string + attach_string
        temp_list = []
        count += 1


build_database()
print("Station to be searched for: ", end = "")
station_name_input = input()
station_name_input = format_input(station_name_input)
find_station(station_name_input)
make_interchange_list()
build_output_line(found_list)
build_output_station(found_list, interchange)
if found_list:
    print(station_name_input + " Station found")
    output_list.sort()
    for item in output_list:
        print(item)
else:
    print("Station not found")
