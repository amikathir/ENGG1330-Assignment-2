# Amaresh Kathiresan ENGG1330 Assignment 2 Level 4 UID: 3035962556
island = []
tsuen_wan = []
east_rail = []
kwun_tong = []
tuen_ma = []
station_DB = {1: island, 2: tsuen_wan, 3: east_rail, 4: kwun_tong, 5: tuen_ma}
station_name_DB = {1: "Island Line", 2: "Tsuen Wan Line", 3: "East Rail Line", 4: "Kwun Tong Line", 5: "Tuen Ma Line"}
found_list = []
interchange = []
route_stations = []
output_list = []
same_line_list = []
unique_station_list = []
final_output_list = []


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
    if name not in island and name not in tsuen_wan and name not in east_rail \
            and name not in kwun_tong and name not in tuen_ma:
        return False
    else:
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
        return True


def check_same_line(check_list):
    list_length = len(check_list)
    if list_length == 2:
        station1 = check_list[0]
        station2 = check_list[1]
        if station1 == station2:
            same_line_list.append(station_name_DB.get(check_list[0]))
    if list_length == 3:
        station1 = check_list[0]
        station2 = check_list[2]
        if station1 == station2:
            same_line_list.append(station_name_DB.get(check_list[0]))
    if list_length == 4:
        station1 = check_list[0]
        station2 = check_list[2]
        if station1 == station2:
            same_line_list.append(station_name_DB.get(check_list[0]))
        station1 = check_list[1]
        station2 = check_list[3]
        if station1 == station2:
            same_line_list.append(station_name_DB.get(check_list[1]))
    if same_line_list:
        same_line_list.sort()
        for item in same_line_list:
            print(item)
        return False
    else:
        return True


def check_interchange_lines(origin, destination, interchange_list):
    return_list = []
    for i in range(1, 6):
        line = station_DB.get(i)
        if origin in line:
            origin_line = line
        if destination in line:
            destination_line = line
    for item1 in interchange_list:
        for item2 in origin_line:
            for item3 in destination_line:
                if item1 == item2 and item1 == item3:
                    return_list.append(item1)
    return return_list


def build_output_line(check_list):
    for item in check_list:
        for j in range(1, 6):
            if item == j:
                output_list.append(station_name_DB.get(j) + ": ")
    output_list.sort()


def build_output_station(route_list, origin, destination):
    global final_output_list
    for i in range(len(route_list)):
        attach_string = origin + "->" + route_list[i]
        attach_string2 = route_list[i] + "->" + destination
        if i != len(route_list) and len(route_list) != 1:
            final_output_list.append(output_list[i] + attach_string)
            final_output_list.append(output_list[i + 1] + attach_string2)
        elif i != len(route_list) - 1:
            final_output_list.append(output_list[i] + attach_string)
            final_output_list.append(output_list[i + 1] + attach_string2)


build_database()
print("Origin station: ", end = "")
origin_station_input = input()
print("Destination station: ", end = "")
destination_station_input = input()
origin_station_input = format_input(origin_station_input)
destination_station_input = format_input(destination_station_input)
station_found = find_station(origin_station_input)
if station_found:
    station_found = find_station(destination_station_input)
    if station_found:
        if check_same_line(found_list):
            make_interchange_list()
            route_stations = check_interchange_lines(origin_station_input, destination_station_input, interchange)
            build_output_line(found_list)
            build_output_station(route_stations, origin_station_input, destination_station_input)
            final_output_list.sort()
            for item in final_output_list:
                print(item)
    else:
        print("Station(s) not found")
else:
    print("Station(s) not found")
