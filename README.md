# DVBSDR
Tools for dvb 
Date : 21.10.2019
Author : Alessio Vacondio (IK4IDY)


Scope : Realize a DVBSDR (F5OEO) launcher, excluding use of third part hardware or Software.

Language : Python and shell.

Since I started to use dvbsdr, i found annoying to change everytime parameters for TX, in scripts files.
For this reason I decided to develop a "launcher", thah has in the main window all the principal parameters for the DVBSDR (F5OEO).
The starting point is from my needs. Now I have Jetson Nano, and Lime Express. I have projected to start, sending a TS via HDMI-LKV converter.
There is a script "jetson_nano.sh" having all parameters to transmit. Normally you need to use an editor to change parameters in the scripts.
With my project you will have window for the launch with all the main parameters, power included. When you select "TX" button, automatically a 
new configuration scripts will be prepared and launched, a "classic" terminal windows will be opened, as usual, to check the stream.
When you want stop, close the terminal window, and at this point you can change parameters in the window or stop the activity. 

Pay attention to the power cursor, if you need to change power you will need to stop and restart, the console windows.

