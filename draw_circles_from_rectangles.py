import rosegraphics as rg
import math


def main():
    window1 = rg.RoseWindow(720, 500, 'Tests 1 and 2 of draw_circles_from_rectangles')
    window2 = rg.RoseWindow(620, 380, 'Test 3 of draw_circles_from_rectangles')
    draw_circles_from_rectangles(window1,400,250,440,325,5,'green','black',4,5)
    draw_circles_from_rectangles(window1,500,450,600,400,3,'blue','red',8,3)
    draw_circles_from_rectangles(window2,350,280,375,330,5,'yellow','brown',6,10)
    window1.render()
    window2.render()
    window1.close_on_mouse_click()
    window2.close_on_mouse_click()


def draw_circles_from_rectangles(window,x1,y1,x2,y2,thick,fill,outcol,nleft,nup):
    rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
    rectangle.fill_color = fill
    rectangle.outline_thickness = thick
    rectangle.outline_color = outcol
    rectangle.attach_to(window)
    rcenter = rectangle.get_center()
    height = rectangle.get_height()
    width = rectangle.get_width()

    circle1=rg.Circle(rg.Point(rcenter.x-((width/2)+(height/2)),rcenter.y),height/2)
    circle1.fill_color=fill
    circle1.attach_to(window)
    ccenter1=circle1.center

    for k in range(nleft-1):
        circleloop1=rg.Circle(rg.Point(ccenter1.x-((k+1)*height),ccenter1.y),height/2)
        circleloop1.fill_color=fill
        circleloop1.attach_to(window)

    circle2 = rg.Circle(rg.Point(rcenter.x, rcenter.y - ((height/2)+(width/2))), width / 2)
    circle2.outline_color=outcol
    ccenter2 = circle2.center
    circle2.attach_to(window)
    for k in range(nup-1):
        circleloop2 = rg.Circle(rg.Point(ccenter2.x, ccenter2.y - ((k + 1) * width)), width / 2)
        circleloop2.outline_color=outcol
        circleloop2.attach_to(window)


main()
