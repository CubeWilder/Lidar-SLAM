from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
import os

def generate_launch_description():
    pkg_dir = os.path.join(os.getenv('HOME'), 'ros2_ws', 'src', 'my_robot_bringup')
    config_dir = os.path.join(pkg_dir, 'config', 'slam_params.yaml')

    return LaunchDescription([
        # Lidar starten
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(os.getenv('HOME'), 'ros2_ws', 'src', 'rplidar_ros', 'launch', 'rplidar_c1_launch.py')
            ])
        ),

        # Statischer TF: base_link -> laser
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_laser_broadcaster',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser']
        ),

        # Optional: Statischer TF odom -> base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='odom_to_base_broadcaster',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
        ),

        # SLAM Toolbox
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[config_dir]
        )
    ])

