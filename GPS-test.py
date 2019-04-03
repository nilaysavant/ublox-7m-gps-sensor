#!/usr/bin/env python

# *** GPS Sensor test ***
#
# Author : Nilay Savant
#
# Description : 
#
import serial, pynmea2

with serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=0.5) as ser:
    try:
        while True:
            line = ser.readline().decode('ascii', errors='replace')
            # print(line.strip())
            if line[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
                msg = pynmea2.parse(line) 
                
                if len(msg.lat) > 0:
                    lat_dec = int(float(msg.lat)/100) + (float(msg.lat)%100)/60
                    lon_dec = int(float(msg.lon)/100) + (float(msg.lon)%100)/60

                    # Create the string to be output from fields
                    output = "lat : " + str(lat_dec) + msg.lat_dir + \
                    "  " + "long : " + str(lon_dec)+ msg.lon_dir +  \
                    "  " + "alt : " + str(msg.altitude) + \
                    "  " + "satellites : " + str(msg.num_sats) + \
                    "  " + "qual : " + str(msg.gps_qual) + \
                    "  " + "stationid : " + str(msg.ref_station_id)
                    
                    # Directly print google maps url
                    output2 = "https://www.google.com/maps/@" + str(lat_dec) + "," + str(lon_dec) + ",60m/data=!3m1!1e3"
                    
                    print output + "\n" + output2 + "\n"
                else:
                    print "satellites : " + str(msg.num_sats) + \
                    "  " + "qual : " + str(msg.gps_qual) + \
                    "  " + "No fix yet"
    except KeyboardInterrupt:
        print "exiting..."