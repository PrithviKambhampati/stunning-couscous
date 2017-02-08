#!/usr/bin/env python
import rospy
import roslaunch
import time
import random


def patroller():
    package = 'gazebo_ros'
    executable = 'spawn_model'
    arguments = '-urdf -model jackal -param robot_description '
    spawn_location = [  '-x 0 -y 0 -z 1.0',
                        '-x 0 -y 7 -z 1.0',
                        '-x 7 -y 7 -z 1.0',
                        '-x 7 -y 0 -z 1.0']

    location = random.choice(spawn_location)
    #location = '-x 0 -y 7 -z 1.0'
    arguments += location

    time.sleep(10)

    node = roslaunch.core.Node(package, executable, args=arguments)

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    process = launch.launch(node)

    print('Spawned at ' + location)
    print(process.is_alive())

    time.sleep(3)
    process.stop()


if __name__ == '__main__':
    patroller()
