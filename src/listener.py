#!/usr/bin/env python
import rospy
import time
from subprocess import call
from std_msgs.msg import String
import threading

my_mutex = threading.Lock()

def callback1(data):

    rospy.loginfo(rospy.get_caller_id() + "callback1: I heard %s", data.data)

    my_mutex.acquire()    
    print "callback1: critical section entering ..."
    for x in range(0, 30):
        call(["sleep", "1"])
    print "callback1: critical section completed ..."
    my_mutex.release() 

def callback2(data):

    rospy.loginfo(rospy.get_caller_id() + "callback2: I heard %s", data.data)

    my_mutex.acquire()
    print "callback2: critical section entering ..."
    for x in range(0, 30):
        call(["sleep", "1"])
    print "callback2: critical section completed ..."
    my_mutex.release()

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

