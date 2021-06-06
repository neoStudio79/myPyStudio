from turtle import *
color("red", "yellow")
begin_fill()
while True:
    forward(180)
    left(168)
    if abs(pos()) < 1:
        break
end_fill()
done()
