# Runner script for all modules

from load_data import load_sensor_data
from house_info import HouseInfo
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
data = load_sensor_data()
print("Loaded records: {}",format(len(data)))
house_info = HouseInfo(data)
##############################

# Module 1 code here:

# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here:
