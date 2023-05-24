import pdb

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D


def get_potential_surface(function, num=200):
    x = np.linspace(function.min_x, function.max_x, num)
    y = np.linspace(function.min_y, function.max_y, num)
    x, y = np.meshgrid(x, y)
    
    dim = len(x)
    energy_l = np.empty((dim, dim))
    for i in range(dim):
        for j in range(dim):
            x_i = x[i, j]
            y_i = y[i, j]
            energy_l[i, j] = function.evaluate(x_i, y_i)

    return x, y, energy_l


def plot_optimization_history(history, function):
    x_history = [i[0] for i in history]
    y_history = [i[1] for i in history]
    z_history = [i[2] for i in history]
    grad_history = [i[3] for i in history]

    x, y, z = get_potential_surface(function)

    # グラフの作成
    fig = plt.figure(figsize=(20, 6))

    # 2次元プロット（等高線プロット）
    ax1 = fig.add_subplot(131)
    ax1.plot(x_history, y_history, 'r.-', zorder=5)

    if function.name == 'muller_brown_potential':
        contour = ax1.contourf(x, y, z, levels=function.levs, cmap='RdBu_r', extend='neither')
    else:
        contour = ax1.contourf(x, y, z, norm=LogNorm(), levels=function.levs, cmap='viridis', extend='neither')

    ax1.set_aspect('equal','box')
    ax1.set_xlabel('x', fontsize=15)
    ax1.set_ylabel('y', fontsize=15)
    ax1.set_xlim(function.min_x, function.max_x)
    ax1.set_ylim(function.min_y, function.max_y)
    ax1.tick_params(labelsize=10)
    ax1.set_title('2D visualization', fontsize=20)

    # 3次元プロット
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.plot(x_history, y_history, z_history, 'r.-', zorder=5)

    mask = z > function.max_f
    z[mask] = function.max_f

    if function.name == 'muller_brown_potential':
        ax2.plot_surface(x, y, z, cmap='RdBu_r', edgecolor='none', alpha=1.0)
    else:
        ax2.plot_surface(x, y, z, cmap='viridis', edgecolor='none', norm=LogNorm(), alpha=1.0)

    ax2.set_xlabel('x', fontsize=15)
    ax2.set_ylabel('y', fontsize=15)
    ax2.set_zlabel('f(x, y)', fontsize=15)
    ax2.set_xlim(function.min_x, function.max_x)
    ax2.set_ylim(function.min_y, function.max_y)
    ax2.set_zlim(function.min_f, function.max_f)
    ax2.tick_params(labelsize=10)
    ax2.set_title('3D visualization', fontsize=20)

    ax3 = fig.add_subplot(133)

    itr = [i for i in range(len(grad_history))]

    ax3.plot(itr, grad_history)
    ax3.set_yscale('log')

    ax3.set_xlabel('Iteration', fontsize=15)
    ax3.set_ylabel('Gradient', fontsize=15)
    ax3.tick_params(labelsize=10)
    ax3.set_title('Gradient history', fontsize=20)

    plt.tight_layout()
    # plt.savefig('Visualization.jpeg')
    plt.show()


def plot_potential_surface(function, elev=30, azim=-60):
    x, y, z = get_potential_surface(function)

    # グラフの作成
    fig = plt.figure(figsize=(12, 5))

    # 2次元プロット（等高線プロット）
    ax1 = fig.add_subplot(121)

    if function.name == 'muller_brown_potential':
        contour = ax1.contourf(x, y, z, levels=function.levs, cmap='RdBu_r', extend='neither')
    else:
        contour = ax1.contourf(x, y, z, norm=LogNorm(), levels=function.levs, cmap='viridis', extend='neither')

    ax1.set_aspect('equal','box')
    ax1.set_xlabel('x', fontsize=15)
    ax1.set_ylabel('y', fontsize=15)
    ax1.set_xlim(function.min_x, function.max_x)
    ax1.set_ylim(function.min_y, function.max_y)
    ax1.tick_params(labelsize=10)
    ax1.set_title('2D visualization', fontsize=20)

    # 3次元プロット
    ax2 = fig.add_subplot(122, projection='3d')

    mask = z > function.max_f
    z[mask] = function.max_f

    if function.name == 'muller_brown_potential':
        ax2.plot_surface(x, y, z, cmap='RdBu_r', edgecolor='none', alpha=1.0)
    else:
        ax2.plot_surface(x, y, z, cmap='viridis', edgecolor='none', norm=LogNorm(), alpha=1.0)

    ax2.set_xlabel('x', fontsize=15)
    ax2.set_ylabel('y', fontsize=15)
    ax2.set_zlabel('f(x, y)', fontsize=15)
    ax2.set_xlim(function.min_x, function.max_x)
    ax2.set_ylim(function.min_y, function.max_y)
    ax2.set_zlim(function.min_f, function.max_f)
    ax2.tick_params(labelsize=10)
    ax2.set_title('3D visualization', fontsize=20)
    ax2.view_init(elev=elev, azim=azim)

    plt.tight_layout()
    plt.savefig('image/' + function.name + '.jpeg')
    # plt.show()
    plt.close()


if __name__ == '__main__':
    from benchmark_funcs import *
    plot_potential_surface(function=Sphere, elev=45, azim=-60)
    plot_potential_surface(function=Rosenblock, elev=40, azim=-85)
    plot_potential_surface(function=Beale, elev=50, azim=-35)
    plot_potential_surface(function=ThreeHumpCamel, elev=40, azim=-65)
    plot_potential_surface(function=Himmelblau, elev=60, azim=-65)
    plot_potential_surface(function=MullerBrownPotential, elev=70, azim=-110)
