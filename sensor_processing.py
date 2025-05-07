
# 1. Average Calculator
def calculate_average(values):
    return sum(values) / len(values)

data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average:", average)

# 2. Stations List & Display
stations = [
    ["A1", 62],
    ["B2", 105],
    ["C3", 98],
    ["D4", 45]
]

for station in stations:
    print(f"{station[0]} → {station[1]}")

# 3. Status Reporter
def report_status(stations, threshold):
    for station in stations:
        name, pm25 = station
        if pm25 > thres

