import rosegraphics as rg

def main():
    window1=rg.RoseWindow(600,350,'Tests 1 & 2 of draw_parallel_lines')
    draw_parallel_lines(window1,50,200,300,4)
    draw_parallel_lines(window1,400,50,100,7)
    window1.render()
    window1.close_on_mouse_click()
    window2=rg.RoseWindow(500,400,'Test 3 of draw_parallel_lines')
    draw_parallel_lines(window2,20,20,470,12)
    window2.render()
    window2.close_on_mouse_click()


def draw_parallel_lines(window,x1,y1,l,n):
    for k in range(n):
        line=rg.Line(rg.Point(x1,y1+(k*30)),rg.Point(x1+l,y1+(k*30)))
        line.attach_to(window)
main()