"""
This is a "client" module for interacting with the `simple_library`. You do
**not** have to name this `client.py` - it can be named anything.
"""

from simple_library import arithmetic, machines

result = arithmetic.compute_sum(1, 2)
print(result)

second_result = arithmetic.compute_difference(2, 1)
print(second_result)

print() # This just prints out a "newline". That is just a blank line on the terminal.

# Let's create a simple CNC machine with three (3) linear axes.

actual_machine = machines.Machine(12.0, 12.0, 12.0)

print("Let's move 1 unit in the positive X-direction.")
actual_machine.move_x_axis(1.0)
print()

print("Let's move 2 units in the negative X-direction.")
# This is obviously an invalid move because we have assumed that the home
# position of all axes is 0.0 and the home position is right up against their
# limit switches in the negative direction. Therefore, any negative absolute
# position of the machine will result in an axis crash (which is bad, clearly).
actual_machine.move_x_axis(-2.0)
print()

print("Where is the X-axis position right now?")
print(actual_machine.x_axis_current_pos)
print()

actual_machine.go_home()

print("Where is the X-axis position right now?")
print(actual_machine.x_axis_current_pos)
print()

# Ok. Now let's create a CNC machine (like before with 3 linear axes) with a
# B-axis (rotary axis).

actual_machine_with_rotary = machines.RotaryMachine(10.0, 10.0, 10.0, 240.0)

print("Let's move 5 degrees in the positive direction for the B-axis.")
actual_machine_with_rotary.rotate_b_axis(5.0)
print()

print("Where is the B-axis right now?")
print(actual_machine_with_rotary.b_axis_current_pos)
print()

print("Let's move 300 degrees in the positive direction for the B-axis.")
actual_machine_with_rotary.rotate_b_axis(300.0)
print()

# This will print 65 degrees. Why?
# Because 5.0 degrees (from the previous move) + 300.0 degrees (from this move)
# will wrap the total of 305 degrees around the maximum B-axis rotation of
# 240.0 degrees. Therefore, the actual position of the B-axis will be
# 305.0 degrees - 240.0 degrees = 65.0 degrees.
print("Where is the B-axis right now?")
print(actual_machine_with_rotary.b_axis_current_pos)
print()

# We know now that the B-axis is at 65.0 degrees. So, let's try to move 100.0 degrees
# in the **negative** direction.
print("Let's move 100 degrees in the negative direction for the B-axis.")
actual_machine_with_rotary.rotate_b_axis(-100.0)
print()

# This will print out 35.0 degrees. Why?
# Because 65 degrees (from the previous move) + -100 degrees (from this move)
# will wrap the total of -35 degrees around 0.0 (B-axis home). Therefore, the
# actual position of the B-axis will be (0.0 degrees) - (-35.0 degrees) =
# +35.0 degrees.
print("Where is the B-axis right now?")
print(actual_machine_with_rotary.b_axis_current_pos)
print()

# Send the B-axis to home (0.0), but also send all of the linear axes home by
# calling the 'go_home' method from the "super" class (which is the "Machine"
# class).
actual_machine_with_rotary.go_home()

print("Where is the B-axis right now?")
print(actual_machine_with_rotary.b_axis_current_pos)
print()