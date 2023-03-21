from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution
import os


def generate_launch_description():
    mater_bringup = get_package_share_directory("mater_bringup")
    
    rviz_config = PathJoinSubstitution([mater_bringup, "rviz", "mater.rviz"])
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config]
    )

    actions = [
        rviz2_node
    ]

    return LaunchDescription(actions)
