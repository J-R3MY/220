"""
Name: Jeremy Miller
traffic.py

Problem: This program analyzes traffic patterns

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    num_roads = eval(input("How many roads were surveyed?"))
    acc1 = 0
    for roads in range(num_roads):
        num_days = eval(input("How many days was road " + str(roads+1) + " surveyed?"))
        acc = 0
        for days in range(num_days):
            num_cars = eval(input("How many cars traveled on day " + str(days+1) + "?"))
            acc = acc + num_cars
        acc1 = acc1 + acc
        road_avg = acc / num_days
        print("Road " + str(roads+1) + " average vehicles per day: ", round(road_avg, 2))
    print("Total number of vehicles traveled on all roads: ", round(acc1, 2))
    vehicle_avg = acc1 / num_roads
    print("Average number of vehicles per road: ", round(vehicle_avg, 2))


if __name__ == '__main__':
    main()
