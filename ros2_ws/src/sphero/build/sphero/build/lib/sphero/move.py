from spherov2.toy.mini import Mini
from spherov2.types import Color
from spherov2 import scanner
from . import spheroapi as SpheroEduAPI
import time

def main():
    toy = scanner.find_Mini()
    print(toy)

    dist = 0

    with SpheroEduAPI.SpheroEduAPI(toy) as droid:   
        while dist <= 1:
            dist = droid.get_distance()
            # Uncomment the following lines if you want to print the distance or do more with it
            # angle = droid.get_orientation()
            # print("Distance:", dist)
            droid.set_speed(120)
            droid.set_heading(90)
            # Add any additional commands or logic here

# Make sure to include this check
if __name__ == '__main__':
    main()
