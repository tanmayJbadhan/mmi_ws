The implementaion is for an interface using a sphero mini robotic toy with IMU and motors connected via bluetooth.   
  Environments and Hardware:
* Sphero Mini: https://sphero.com/products/sphero-mini
* The sphero minio is an exiting toy for robotic eduction but the BLE(Bluetooth Low Energy) toys are closed source and they share a specific handshaking mechanism for bluetooth connection. 
* I tweaked this library: https://github.com/artificial-intelligence-class/spherov2.py to work with sphero mini (and with Python 3.8)
* Empy errors: The current verison of empy(4.0) is not supported in ROS2 on windows, I downgraded it to empy(3.3)
* Other Dependencies:  
PyautoGUI: Uses to control Mouse Pointer movement.

The Publisher-Subscriber Model:  
1. Arduino connected to COM port and continously publishing IR Serial Data.
2. The Serial data is read by a ROS2 publisher which is written in python and build into a package named "IRpublisher" 
3. A ROS2 subscriber reads the data form topic and runs a python script which uses spherov2 library and the sphero is contolled by defining actions mapped to different keys in the IR remote.
4. The nodes irpublisher and sphero are used for demonsration.
5. https://www.youtube.com/watch?v=sEJilginecY&ab_channel=TanmayBadhan

Mouse Pointer Control Model:  
1. A Ros2 package is srripted to map the IMU orientation values of ROLL, PITCH to the mouse pointer.
2. To simulate left and right click different orientaion patterns are defined and a classifer is used to predict the action.
3. The interrupt handling in this implementaion has errors so the demo for (2) is not recorded.
4. The node sphero mouse is used for demonstration
5. https://www.youtube.com/shorts/9XeHiKcFEeU

