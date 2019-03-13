import rosegraphics as rg

def main():
    window1=rg.RoseWindow(900,400,'Tests 1 & 2 of draw_lines_from_rectangles')
    window2=rg.RoseWindow(700,700,'Test 3 of draw_lines_from_rectangles')
    draw_lines_from_rectangles(window1,100,25,150,125,300,150,400,175,'red','blue',5)
    draw_lines_from_rectangles(window1,870,30,750,100,700,90,650,60,'black','green',8)
    draw_lines_from_rectangles(window2,100,25,150,125,300,150,400,175,'cyan','brown',11)
    window1.render()
    window2.render()
    window1.close_on_mouse_click()
    window2.close_on_mouse_click()

def draw_lines_from_rectangles(window, x1, y1, x2, y2, x3, y3, x4, y4, col1, col2, n):
    rec1=rg.Rectangle(rg.Point(x1, y1),rg.Point(x2, y2))
    rec1.outline_color=col1
    rec1.attach_to(window)
    center1=rec1.get_center()
    width1=rec1.get_width()
    height1=rec1.get_height()
    rec2 = rg.Rectangle(rg.Point(x3, y3), rg.Point(x4, y4))
    rec2.outline_color = col2
    rec2.attach_to(window)
    center2 = rec2.get_center()
    for k in range(n):
        line=rg.Line(rg.Point(center1.x-(k*(width1/2)),center1.y+(k*(height1/2))),rg.Point(center2.x-(k*(width1/2)),center2.y+(k*(height1/2))))
        if k%2==0:
            line.color=col1
        else:
            line.color=col2
        line.attach_to(window)
main()