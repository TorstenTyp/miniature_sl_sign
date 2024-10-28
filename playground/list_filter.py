import re

metro_stations = open("metro_stations.txt", "r", encoding='utf-8')
stations = open("stationer.txt", "r", encoding='utf-8')
filtered_stations = open("nya_stationer.txt", "r", encoding='utf-8')

metro = []
new_metro = []

# for station in metro_stations:
#     metro.append(station.strip('\n'))

for station in filtered_stations:
    new_metro.append(station.strip('\n'))

# print(metro)
# print(sorted(new_metro))

for line in sorted(new_metro):
    # if line not in new_metro:
    print(line)

metro_stations.close()
stations.close()