from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='kachaka_pose_listener',
            executable='pose_listener',
            name='pose_listener',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '' ]  # デフォルト設定で起動。必要に応じてrviz設定ファイルを指定可
        )
    ])
