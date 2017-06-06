#!/usr/bin/env python
import rospy
import time
from subprocess import call
from std_msgs.msg import String

flag0 = 0
def callback1(data):
    global flag0 

    rospy.loginfo(rospy.get_caller_id() + "callback1: I heard %s", data.data)
    
    while (flag0 == 1):
        time.sleep(0.1)
    
    print "callback1: critical section entering ..."
    flag0 = 1
    for x in range(0, 30):
        call(["sleep", "1"])
    print "callback1: critical section completed ..."
    flag0 = 0

def callback2(data):
    global flag0

    rospy.loginfo(rospy.get_caller_id() + "callback2: I heard %s", data.data)

    while (flag0 == 1):
        time.sleep(0.1)

    print "callback2: critical section entering ..."
    flag0 = 1
    for x in range(0, 30):
        call(["sleep", "1"])
    print "callback2: critical section completed ..."
    flag0 = 0

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("topic1", String, callback1)
    rospy.Subscriber("topic2", String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

