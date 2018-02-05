#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from math import pi

rospy.init_node('laser_scan_publisher')

scan_pub = rospy.Publisher('scan', LaserScan, queue_size=50)

num_readings = 100
laser_frequency = 10

count = 0
r = rospy.Rate(10)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    scan = LaserScan()

    scan.header.stamp = current_time
    scan.header.frame_id = 'base_laser'
    scan.angle_min = 0
    scan.angle_max = 2*pi
    scan.angle_increment = 2*pi / num_readings
    scan.time_increment = (1.0 / laser_frequency) / (num_readings)
    scan.range_min = 0.0
    scan.range_max = 1000.0

    scan.ranges = []
    scan.intensities = []
    for i in range(0, num_readings):
        scan.ranges.append(1.0 * count)  # fake data
        scan.intensities.append(1)  # fake data

    scan_pub.publish(scan)
    count += 1
    r.sleep()