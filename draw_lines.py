import rosegraphics as rg
import math

def main():
    window1=rg.RoseWindow(350,400,'Tests 1 and 2 of draw_lines')

    draw_lines(window1,50,200,4)
    draw_lines(window1,150,230,12)


    window1.render()

    window1.close_on_mouse_click()

def draw_lines(window,x1,y1,n):
    for k in range(n):
        x2=x1+100
        y2=-1*(x2-x1)+y1
        line=rg.Line(rg.Point(x1,y1),rg.Point(x2,y2-(k*((y2-y1)/(n+1)))))
        line.attach_to(window)

main()