"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Brandon Hao.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

john = rg.SimpleTurtle('turtle')
john.pen = rg.Pen('pink', 3)
john.speed=20

xa=0
ya=0

john.left(125)
for i in range (5):
    for k in range(24):
        john.forward(10)
        john.left(8)
    john.forward(158)

    john.pen_up()
    john.go_to(rg.Point(xa , ya))
    john.right(260)

    john.pen_down()
    for j in range(24):
        john.forward(10)
        john.right(8)
    john.forward(156)

    john.pen_up()
    john.left(260)

    xa=xa+5
    ya=ya+8
    john.go_to(rg.Point(xa, ya))

    john.pen_down()

john.left(90)
john.pen_up()
john.go_to(rg.Point(140,100))
john.pen_down()
john.go_to(rg.Point(104,64))
john.pen_up()
john.go_to(rg.Point(0,-40))
john.pen_down()
john.go_to(rg.Point(-140,-180))

window.close_on_mouse_click()


