#!/usr/bin/env python

import rospy
from crazyflie_clients_python.msg import oa
import random


rospy.init_node('range_publisher')

range_pub = rospy.Publisher('ranges', oa, queue_size=10)

r = rospy.Rate(10)

while not rospy.is_shutdown():
    data = oa()
    data.rangeFront = random.randint(0,1000)
    data.rangeRight = random.randint(0, 1000)
    data.rangeBack = random.randint(0, 1000)
    data.rangeLeft = random.randint(0, 1000)

    range_pub.publish(data)
    r.sleep()