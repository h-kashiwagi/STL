# -*- mode: python -*-
# UnKnown Wordという波線は、スペルチェッカーのものですので、
# モジュールの有り無しとは関係ありません。
import pyvista as pv
import numpy as np
import tkinter
from tkinter import filedialog

# STLの拡大／縮小
def magnification(points, Mx, My, Mz):
    M = np.array([Mx, My, Mz])
    for i in range(3):
        points[:, i] = points[:, i] * M[i]
    return points

def getfile():
    idir = 'C:\\Users\\t-tsutsumi\\Documents\\work\Python練習'
    file_type = [("STLファイル","*.stl"),("すべて","*")]
    file_path = tkinter.filedialog.askopenfilename(filetypes = file_type, initialdir = idir)
    return file_path

# STLファイルの選択と読み込み
mesh_0 = pv.read(getfile())
mesh_1 = pv.read(getfile())

# STLファイルの結合
mesh_2 = mesh_0 + mesh_1
# points = mesh_aft.points
# mesh_aft.points = magnification(points, 1, 2, 1)

# STLファイルの保存
pv.save_meshio('new.stl', mesh_2)

# Multi Window Plot
plotter = pv.Plotter(shape='2|1')

# Window 0
plotter.subplot(0)
plotter.add_text("1'st of stl file", font_size=20)
plotter.add_mesh(mesh_0)
plotter.add_axes(interactive=True)

# Window 1
plotter.subplot(1)
plotter.add_text("2'nd of stl file", font_size=20)
plotter.add_mesh(mesh_1)
plotter.add_axes(interactive=True)

# Window 2
plotter.subplot(2)
plotter.add_text("add of stl file", font_size=20)
plotter.add_mesh(mesh_2)
plotter.add_axes(interactive=True)

# Display the Window
plotter.show()