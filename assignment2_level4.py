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
origin_line = []
destination_line = []


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
    origin_line_name = []
    destination_line_name = []
    return_list = []
    for i in range(1, 6):
        line = station_DB.get(i)
        if origin in line:
            origin_line.append(line)
            origin_line_name.append(station_name_DB.get(i))
        if destination in line:
            destination_line.append(line)
            destination_line_name.append(station_name_DB.get(i))
    for item1 in interchange_list:
        for j in range(len(origin_line)):
            for k in range(len(destination_line)):
                if item1 in origin_line[j] and item1 in destination_line[k]:
                    return_list.append([origin_line_name[j], destination_line_name[k], item1])
    return return_list


def build_output_station(route_list, origin, destination):
    for item2 in route_list:
        start_line = item2[0]
        end_line = item2[1]
        interchange_station = item2[2]
        output_list.append(start_line + ": " + origin + "->" + interchange_station)
        output_list.append(end_line + ": " + interchange_station + "->" + destination)


def sort_route_list(item1):
        return item1[2]


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
            route_stations = sorted(route_stations, key  = sort_route_list)
            if route_stations:
                build_output_station(route_stations, origin_station_input, destination_station_input)
                for item in output_list:
                    print(item)
            else:
                print("More than one change or no route found")
    else:
        print("Station(s) not found")
else:
    print("Station(s) not found")
