import rosegraphics as rg

def main():
    window1=rg.RoseWindow(650,350,'Tests 1 & 2 of draw_squares_from_circle')
    draw_squares_from_circle(window1,100,100,20,'green',7)
    draw_squares_from_circle(window1,350,70,50,None,4)
    window1.render()
    window1.close_on_mouse_click()
    window2=rg.RoseWindow(525,300,'Test 3 of draw_squares_from_circle')
    draw_squares_from_circle(window2,50,50,10,'blue',20)
    window2.render()
    window2.close_on_mouse_click()

def draw_squares_from_circle(window,x1,y1,rad,col,n):
    circle=rg.Circle(rg.Point(x1,y1),rad)
    circle.fill_color=col
    circle.attach_to(window)
    for k in range(n):
        square=rg.Square(rg.Point(x1+(k*rad),y1+(k*rad)),2*rad)
        square.attach_to(window)
main()