# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n = 1000
# 网格化
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(
    -x ** 2 - y ** 2)
mp.figure('3D Surface')
# 创建三维坐标系
ax = mp.gca(projection='3d')  # 返回axes3d类的对象
mp.title('3D Surface', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制三维表面图
ax.plot_surface(x, y, z, rstride=10, cstride=10,
                cmap='jet')
mp.figure('3D Wireframe')
# 创建三维坐标系
ax = mp.gca(projection='3d')  # 返回axes3d类的对象
mp.title('3D Wireframe', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制三维线框图
ax.plot_wireframe(x, y, z, rstride=30, cstride=30,
                  linewidth=0.5, color='dodgerblue')
mp.show()
