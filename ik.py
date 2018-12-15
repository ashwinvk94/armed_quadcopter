#!/usr/bin/python
'''
The armed quadcopter Inverse Kinematics Demo. PLeaese refer to https://github.com/ashwinvk94/armed_quadcopter usage documentation
__author__ = "Ashwin Varghese Kuruttukulam"
__version__ = "1.0.0"
__maintainer__ = "Ashwin Varghese Kuruttukulam"
__email__ = "ashwinvk94atgmaildotcom"
__status__ = "Demonstration"
'''
import vrep
import quad_helper
import numpy as np
import time
import math

quad_functions = None
try:
	vrep.simxFinish(-1)
	clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
	if clientID != -1:
		vrep.simxSetIntegerSignal(clientID,'gripper_pos',0,vrep.simx_opmode_oneshot)
		quad_functions = quad_helper.quad_helper(clientID)
		print('Main Script Started')
		quad_functions.init_sensors()
		quad_functions.start_sim()
		#Setting initial time
		init_time = time.time()
		d1=0
		while vrep.simxGetConnectionId(clientID) != -1:
			elapsed_time = time.time()-init_time
			#Setting model parameters and link lengths
			h = 0.1
			l1 = 0
			l2 = 0.18
			d_rt = 0.2
			y_off = 0.023
			#Getting object position with respect to first joint
			obj_pos = quad_functions.get_obj_pos()
			#Getting object orientation with respect to first joint
			obj_orien = quad_functions.get_obj_orien()
			#Inverse Kinematics
			joint_pos = quad_functions.get_joint_pos(obj_orien)
			joint_pos = [joint_pos[0],-joint_pos[1],joint_pos[2]]
			theta1 = joint_pos[1]
			theta2 = joint_pos[2]
			x = -l1- l2* math.cos(theta1) - d_rt
			y = -y_off
			z =  h-l2* math.sin(theta1)
			quad_pos = np.array(obj_pos) + np.array([x,y,z])
			if elapsed_time>10:
				if d1<d_rt:
					d1 = d1+0.001
				joint_pos[0] = d1
			#Moving joint as per Inverse Kinematics output
			quad_functions.set_joint_pos(joint_pos)
			quad_functions.move_quad(quad_pos)
			vrep.simxSynchronousTrigger(clientID);
	else:
		print "Failed to connect to remote API Server"
		quad_functions.stop_sim()
		vrep.simxFinish(clientID)

except KeyboardInterrupt:
	quad_functions.stop_sim()
	vrep.simxFinish(clientID)
