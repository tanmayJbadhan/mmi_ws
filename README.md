The implementaion is for an interface using a sphero mini robotic toy with IMU and motors connected via bluetooth. 
Environments and Hardware:
* Sphero Mini: https://sphero.com/products/sphero-mini
* The sphero minio is an exiting toy for robotic eduction but the BLE(Bluetooth Low Energy) toys are closed source and they share a specific handshaking mechanism for bluetooth connection. 
* I tweaked this library: https://github.com/artificial-intelligence-class/spherov2.py to work with sphero mini (and with Python 3.8)
* Empy errors: The current verison of empy(4.0) is not supported in ROS2 on windows, I downgraded it to empy(3.3)
* Other Dependencies:  
PyautoGUI: Uses to control Mouse Pointer movement. 


