import rosegraphics as rg
import math

def main():
    window1=rg.RoseWindow(350,400,'Tests 1 and 2 of draw_lines')
    draw_lines(window1,50,200,4)
    window1.render()
    window1.close_on_mouse_click()

def draw_lines(window,x1,y1,n):
    for k in range(n):
        line=rg.Line(rg.Point(x1,y1),rg.Point(x1+50,y1+(k*0.5)-150))
        line.attach_to(window)

main()