# Solution for the Reeborg robot maze.print
# This is the site: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# # Prepare to track the loop
# loop = 0
# while not at_goal():
#     # Only go into this if reeborg is stuck walking in a circle. If he is, start making him walk in a straight line for awhile.
#     if loop > 4:
#         while front_is_clear():
#             move()
#     if right_is_clear():
#         turn_right()
#         move()
#         loop += 1
#     elif front_is_clear():
#         move()
#         # Reset the loop counter since this means he is out of the loop.
#         loop = 0
#     else:
#         turn_left()
#         loop = 0