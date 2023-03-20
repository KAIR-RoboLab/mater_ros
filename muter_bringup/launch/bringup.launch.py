from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
import os


def generate_launch_description():
    serial_port = LaunchConfiguration("serial_port")
    declare_serial_port_arg = DeclareLaunchArgument(
        "serial_port",
        default_value="/dev/ttyUSB1",
        description="Which serial port to use",
    )

    rviz = LaunchConfiguration("rviz")
    declare_rviz_arg = DeclareLaunchArgument(
        "rviz",
        default_value="False",
        description="Whether to launch RViz2",
    )

    muter_bringup = get_package_share_directory("muter_bringup")
    muter_description = get_package_share_directory("muter_description")

    rosbot_model_path = os.path.join(muter_description, "urdf", "muter.urdf")
    with open(rosbot_model_path, 'r') as infp:
        robot_description_content = infp.read()

    robot_description = {"robot_description": robot_description_content}

    ekf_config = PathJoinSubstitution([muter_bringup, "config", "ekf.yaml"])
    robot_localization_node = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_filter_node",
        output="screen",
        parameters=[ekf_config],
    )

    micro_ros_agent_node = Node(
        package="micro_ros_agent",
        executable="micro_ros_agent",
        name="micro_ros_agent",
        output="screen",
        arguments=["serial", "--dev", "/dev/ttyUSB1", "-b", "576000"],
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
    )

    rviz2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    muter_bringup,
                    "launch",
                    "rviz2.launch.py",
                ]
            )
        ),
        condition=IfCondition(rviz),
    )

    actions = [
        declare_serial_port_arg,
        declare_rviz_arg,
        robot_state_publisher_node,
        robot_localization_node,
        micro_ros_agent_node,
        rviz2_launch,
    ]

    return LaunchDescription(actions)
