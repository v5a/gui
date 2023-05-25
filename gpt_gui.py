import pygame
import tkinter as tk
from pygame.locals import *
from tkinter import *
import os

# Pygame窗口的大小
WIDTH = 500
HEIGHT = 500

# Tkinter窗口设置
root = tk.Tk()

# 创建左侧容器用于放置按钮和多选框
left_container = tk.Frame(root)
left_container.pack(side='left')

# 创建按钮
button1 = tk.Button(left_container, text="打开文件夹",width=20,height=2)
button1.pack(padx=20, pady=50)

button2 = tk.Button(left_container, text="保存",width=20,height=2)
button2.pack(padx=20, pady=50)

# 创建多选框
var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(left_container, text="多边形", variable=var1)
checkbox1.pack(padx=50, pady=10)

var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(left_container, text="矩形框", variable=var2)
checkbox2.pack(padx=50, pady=10)

# 创建右侧容器用于放置文本输入框、按钮和列表框
right_container = tk.Frame(root)
right_container.pack(side='right')

# 创建文本输入框
entry = tk.Entry(right_container, width=30)
entry.pack(padx=10, pady=10)

# 创建按钮
button = tk.Button(right_container, text="提交")
button.pack(padx=10, pady=10)

# 创建用于显示标签的列表框
label_listbox = tk.Listbox(right_container)
label_listbox.pack(padx=10, pady=10)

# 创建用于显示文件名的列表框
filename_listbox = tk.Listbox(right_container)
filename_listbox.pack(padx=10, pady=10)


# 创建Pygame窗口的容器
frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
frame.pack(fill="both", padx=10, pady=10)
frame.pack(expand=1) 


# Pygame设置
os.environ['SDL_WINDOWID'] = str(frame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.init()

# 加载背景图像
background = pygame.image.load('image/123.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # 缩放图像以适应屏幕

# 初始化背景图像的缩放比例
scale_factor = 1.0

# 用于绘制绿点的列表
green_points = []

# 标志用于表示鼠标右键是否正在拖拽
dragging = False
dragging_offset = (0, 0)

# 在Pygame中处理鼠标点击事件
def handle_mouse_event(event):
    global scale_factor
    global green_points
    global dragging
    global dragging_offset
    # 根据缩放比例计算缩放后的背景图像矩形
    scaled_width = int(WIDTH * scale_factor)
    scaled_height = int(HEIGHT * scale_factor)
    scaled_background = pygame.transform.scale(background, (scaled_width, scaled_height))
    scaled_background_rect = scaled_background.get_rect()
    scaled_background_rect.center = screen.get_rect().center
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # 鼠标左键点击
            # 将绿点的位置保存为相对于原始窗口大小的位置
            original_x = int((event.pos[0]-scaled_background_rect[0])/scale_factor)
            original_y = int((event.pos[1]-scaled_background_rect[1])/scale_factor)
            if scaled_background_rect.collidepoint(event.pos):  # 检查点击位置是否在图片区域内
                green_points.append((original_x, original_y))  # 添加一个新的点到列表中
        elif event.button == 2:  # 鼠标中键点击
            green_points.clear()  # 清空点的列表
        elif event.button == 3:  # 鼠标右键点击
            if scaled_background_rect.collidepoint(event.pos):  # 检查点击位置是否在图片区域内
                dragging = True
                dragging_offset = (scaled_background_rect.x - event.pos[0], scaled_background_rect.y - event.pos[1])
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 4:  # 鼠标滚轮向上滚动
            scale_factor *= 1.1  # 增加缩放比例
            # 限制缩放范围
            scale_factor = max(0.1, min(10.0, scale_factor))
        elif event.button == 5:  # 鼠标滚轮向下滚动
            scale_factor /= 1.1  # 减小缩放比例
            # 限制缩放范围
            scale_factor = max(0.1, min(10.0, scale_factor))
        elif event.button == 3:  # 鼠标右键释放
            dragging = False
            dragging_offset = (0, 0)  # 重置拖拽偏移量
    # elif event.type == pygame.MOUSEMOTION:
    #     if dragging:
    #         scaled_background_rect.x = event.pos[0] + dragging_offset[0]
    #         scaled_background_rect.y = event.pos[1] + dragging_offset[1]



        # 绘制Pygame窗口
        screen.fill((255, 255, 255))
        screen.blit(scaled_background, scaled_background_rect)

        # 绘制缩放后的绿点
        for point in green_points:
            scaled_x = int(point[0] * scale_factor)
            scaled_y = int(point[1] * scale_factor)
            pygame.draw.circle(screen, (0, 255, 0), (scaled_x, scaled_y), 5)

        # 绘制水平线
        mouse_y = pygame.mouse.get_pos()[1]
        pygame.draw.line(screen, (0, 255, 255), (0, mouse_y), (WIDTH, mouse_y))

        # 绘制垂直线
        mouse_x = pygame.mouse.get_pos()[0]
        pygame.draw.line(screen, (0, 255, 255), (mouse_x, 0), (mouse_x, HEIGHT))

        pygame.display.update()

# 绘制Pygame窗口的函数
def draw_pygame_window():


    # 清空屏幕
    screen.fill((255, 255, 255))

    # 计算缩放后的背景图像矩形
    scaled_width = int(WIDTH * scale_factor)
    scaled_height = int(HEIGHT * scale_factor)
    scaled_background = pygame.transform.scale(background, (scaled_width, scaled_height))
    scaled_background_rect = scaled_background.get_rect()
    scaled_background_rect.center = screen.get_rect().center

    # 如果正在拖拽，那么根据鼠标的位置和拖拽的偏移量来调整图像的位置
    if dragging:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        scaled_background_rect.x = mouse_x + dragging_offset[0]
        scaled_background_rect.y = mouse_y + dragging_offset[1]
    else:
    #     # 如果没有在拖拽，那么图像居中显示
        scaled_background_rect.center = screen.get_rect().center
    
    
    # 绘制背景图像
    screen.blit(scaled_background, scaled_background_rect)

    # 绘制缩放后的绿点
    for point in green_points:
        scaled_x = int(scaled_background_rect[0]) + int(point[0] * scale_factor)
        scaled_y = int(scaled_background_rect[1]) + int(point[1] * scale_factor)
        pygame.draw.circle(screen, (0, 255, 0), (scaled_x, scaled_y), 5)



    # 绘制水平线
    mouse_y = pygame.mouse.get_pos()[1]
    pygame.draw.line(screen, (0, 255, 255), (0, mouse_y), (frame.winfo_width(), mouse_y))

    # 绘制垂直线
    mouse_x = pygame.mouse.get_pos()[0]
    pygame.draw.line(screen, (0, 255, 255), (mouse_x, 0), (mouse_x, frame.winfo_height()))

    pygame.display.update()


# 在Tkinter事件循环中处理Pygame事件
while True:
    for event in pygame.event.get():
        handle_mouse_event(event)
    draw_pygame_window()
    root.update()