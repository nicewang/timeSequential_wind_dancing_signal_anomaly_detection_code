import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个图像对象
fig, ax = plt.subplots()

# 添加一个圆形表示小熊的头部
circle = patches.Circle((0.5, 0.6), 0.2, color='brown')
ax.add_patch(circle)

# 添加一个矩形表示小熊的身体
rect = patches.Rectangle((0.3, 0.1), 0.4, 0.5, color='brown')
ax.add_patch(rect)

# 添加两个圆形表示小熊的耳朵
left_ear = patches.Circle((0.4, 0.7), 0.08, color='white')
right_ear = patches.Circle((0.6, 0.7), 0.08, color='white')
ax.add_patch(left_ear)
ax.add_patch(right_ear)

# 添加一个矩形表示汽车的车身
car_body = patches.Rectangle((0.2, 0), 0.6, 0.2, color='lightblue')
ax.add_patch(car_body)

# 添加两个圆形表示汽车的轮子
left_wheel = patches.Circle((0.3, 0.1), 0.1, color='black')
right_wheel = patches.Circle((0.7, 0.1), 0.1, color='black')
ax.add_patch(left_wheel)
ax.add_patch(right_wheel)

# 设置图像的坐标轴范围和比例
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# 隐藏坐标轴
plt.axis('off')

# 显示图像
plt.show()
