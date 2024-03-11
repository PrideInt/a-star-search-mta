import csv

# [station_name, tuple coordinates, trains list]
stations = []

with open('mta_stations.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        trains = [row[4]]

        if (len(row) > 5):
            for i in range(5, len(row)):
                trains.append(row[i])

        coordinates = row[3][7:-1].split(' ')
        try:
            stations.append([row[2], (float(coordinates[0]), float(coordinates[1])), trains])
        except:
            print()

# def graph(stations):
    # Apply and validate stations
    # Then turn our stations into a graph

# Takes from index and to index and returns a path
def a_star_search(stations, from_, to):
    # Write the A* search algorithm here
    return ""

# graph(stations)