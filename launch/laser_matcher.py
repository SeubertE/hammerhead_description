import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='ros2_laser_scan_matcher').find('ros2_laser_scan_matcher')
    parameter_file = LaunchConfiguration('params_file')


    robot_laser_matercher_node = launch_ros.actions.Node(
        package='ros2_laser_scan_matcher',
        executable='laser_scan_matcher',
        parameters=[parameter_file]
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='params_file', default_value=''),
        robot_laser_matercher_node
    ])