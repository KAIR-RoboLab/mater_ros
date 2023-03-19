from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import  DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition
import os


def generate_launch_description():
    muter_bringup = get_package_share_directory("muter_bringup")
    
    rviz_config = PathJoinSubstitution([muter_bringup, "rviz", "muter.rviz"])
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config]
    )

    actions = [
        rviz2_node
    ]

    return LaunchDescription(actions)
