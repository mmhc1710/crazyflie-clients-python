#!/usr/bin/env python

from crazyflie_clients_python.msg import oa
from crazyflie_clients_python.srv import oa_srv, oa_srvResponse
import rospy

data = oa()

def handle_get_state(msg):
    # print("Returning [{0} + {1} = {2}]".format(req.a, req.b, (req.a + req.b)))
    rospy.loginfo(msg)
    data.rangeFront = msg.rangeFront
    data.rangeBack = msg.rangeBack
    data.rangeRight = msg.rangeRight
    data.rangeLeft = msg.rangeLeft


    # return oa_srvResponse(req.a + req.b)

def handle_send_state(req):
    # print("Returning [{0} + {1} = {2}]".format(req.a, req.b, (req.a + req.b)))
    return oa_srvResponse(data.rangeFront, data.rangeBack, data.rangeRight, data.rangeLeft)

def get_state_server():
    rospy.init_node('get_state_server')
    srv = rospy.Service('get_state', oa_srv, handle_send_state)
    sub = rospy.Subscriber('chatter', oa, handle_get_state)
    rospy.loginfo("Ready to get state.")
    rospy.spin()

if __name__ == "__main__":
    get_state_server()