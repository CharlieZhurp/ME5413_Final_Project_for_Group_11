#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path, OccupancyGrid
from geometry_msgs.msg import PoseStamped
from astar_planner.astar import AStarPlanner

class AstarPlannerROS:

    def __init__(self):
        # 初始化ROS节点
        rospy.init_node('astar_planner_node')

        # 订阅地图的话题
        rospy.Subscriber('/map', OccupancyGrid, self.map_callback)

        # 订阅目标点的话题
        rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goal_callback)

        # 创建路径规划结果的发布者
        self.path_pub = rospy.Publisher('/astar_planner_node/path', Path, queue_size=10)

        # 创建A*路径规划器对象
        self.astar_planner = AStarPlanner()

    def map_callback(self, map):
        # 处理接收到的地图数据
    
        # 将地图数据转换为二维数组
        map_data = []
        for i in range(map.info.width):
            row = []
            for j in range(map.info.height):
                row.append(map.data[i + j*map.info.width])
            map_data.append(row)
    
        # 初始化A*路径规划器
        self.astar_planner.initialize(map_data, map.info.resolution, map.info.origin)
        
    def goal_callback(self, goal):
        # 处理接收到的目标点，生成路径规划结果
        start = (0, 0)  # 起点固定为(0, 0)
        goal = (int((goal.pose.position.x - self.astar_planner.origin_x) / self.astar_planner.resolution),
                int((goal.pose.position.y - self.astar_planner.origin_y) / self.astar_planner.resolution))
        path = self.astar_planner.plan(start, goal)

        # 将路径规划结果转换为ROS消息格式
        ros_path = Path()
        ros_path.header.frame_id = "map"
        for node in path:
            pose = PoseStamped()
            pose.pose.position.x = node[0] * self.astar_planner.resolution + self.astar_planner.origin_x
            pose.pose.position.y = node[1] * self.astar_planner.resolution + self.astar_planner.origin_y
            pose.pose.orientation.w = 1.0
            ros_path.poses.append(pose)

        # 发布路径规划结果
        self.path_pub.publish(ros_path)


       

