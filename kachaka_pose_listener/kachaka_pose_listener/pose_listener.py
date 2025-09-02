import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
from geometry_msgs.msg import TransformStamped
from tf_transformations import euler_from_quaternion


class PoseListener(Node):
    def __init__(self):
        super().__init__('pose_listener')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.get_pose)

    def get_pose(self):
        try:
            now = rclpy.time.Time()
            transform: TransformStamped = self.tf_buffer.lookup_transform(
                'map', 'base_footprint', now
            )
            x = transform.transform.translation.x
            y = transform.transform.translation.y
            q = transform.transform.rotation
            _, _, yaw = euler_from_quaternion([q.x, q.y, q.z, q.w])
            stamp = transform.header.stamp
            self.get_logger().info(
                f"Time: {stamp.sec}.{stamp.nanosec}, x: {x:.2f}, y: {y:.2f}, yaw: {yaw:.2f}"
            )
        except Exception as e:
            self.get_logger().warn(f"Transform not available: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = PoseListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
