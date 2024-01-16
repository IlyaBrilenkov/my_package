from launch import LaunchDescription
from launch_ros_actions import Node

def generte_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    ])