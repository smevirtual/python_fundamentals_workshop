"""
Various classes to describe factory machines.
"""

class Machine(object):
    """
    Generic factory CNC Machine.

    Parameters
    ----------
    x_travel_max
        Maximum absolute travel for the X-axis from the home position.
    y_travel_max
        Maximum absolute travel for the Y-axis from the home position.
    z_travel_max
        Maximum absolute travel for the Z-axis from the home position.

    Please note. We have only defined an actual move method for the X-axis. In
    practice, you would obviously define methods for all three axes.
    """

    def __init__(self, x_travel_max: float, y_travel_max: float, z_travel_max: float):
        self.x_travel_max = x_travel_max
        self.y_travel_max = y_travel_max
        self.z_travel_max = z_travel_max
        self.x_axis_current_pos = 0.0
        self.y_axis_current_pos = 0.0
        self.z_axis_current_pos = 0.0
        # You cannot have a return here.

    def go_home(self):
        """
        Send all axes home.
        """
        self.x_axis_current_pos = 0.0
        self.y_axis_current_pos = 0.0
        self.z_axis_current_pos = 0.0

    def move_x_axis(self, x_move: float):
        """
        Command a move to the X-axis.

        Parameters
        ----------
        x_move
            Positive or negative move command for the X-axis.
        """
        print("The x-axis is currently at", self.x_axis_current_pos)
        temporary_move = self.x_axis_current_pos + x_move
        # Perform some validation.
        if temporary_move > self.x_travel_max or temporary_move < 0.0:
            print("Invalid move.")
        else:
            self.x_axis_current_pos = temporary_move
            print("The x-axis is now at", self.x_axis_current_pos)

# Inheritence. Is-a relationship.

class RotaryMachine(Machine):
    """
    CNC machine with a rotary table (B-axis).

    Parameters
    ----------
    x_travel_max
        Maximum absolute travel for the X-axis from the home position.
    y_travel_max
        Maximum absolute travel for the Y-axis from the home position.
    z_travel_max
        Maximum absolute travel for the Z-axis from the home position.
    b_axis_rot_max
        Maximum absolute rotation for the B-axis from the home position (in degrees).

    Raises
    ------
    ValueError
        If `b_axis_rot_max` is negative or is greater than 360 degrees.
    """

    def __init__(self, x_travel_max: float, y_travel_max: float,
                 z_travel_max: float, b_axis_rot_max: float):
        Machine.__init__(self, x_travel_max, y_travel_max, z_travel_max)
        if b_axis_rot_max <= 0.0:
            raise ValueError("The maximum rotation of the B-axis cannot be negative.")
        elif b_axis_rot_max > 360.0:
            raise ValueError("The maximum rotation of the B-axis cannot be greater than 360 degrees.")
        self.b_axis_rot_max = b_axis_rot_max
        self.b_axis_current_pos = 0.0

    def go_home(self):
        """
        Send all axes home (including the B-axis).
        """
        super().go_home() # Calling the 'go_home' method in the "super" class (the "Machine" class above).
        self.b_axis_current_pos = 0.0

    def rotate_b_axis(self, b_axis_move: float):
        """
        Command a rotation to the B-axis.

        If the commanded move exceeds the absolute positive limits of the rotary
        table, the actual stored position of the rotary table will flip back
        within range.
        
        For example, if the rotary table has a maximum rotary of
        180 degrees and a 240 degree rotation is commanded, then the actual
        position of the rotary table will be 60 degrees
        (240 degrees - 180 degrees).

        Parameters
        ----------
        b_axis_move
            Positive or negative rotation command for the B-axis (in degrees).
        """
        temporary_rotation = self.b_axis_current_pos + b_axis_move

        if (temporary_rotation > self.b_axis_rot_max):
            self.b_axis_current_pos = temporary_rotation - self.b_axis_rot_max
        elif (temporary_rotation < 0.0):
            self.b_axis_current_pos = 0.0 - temporary_rotation
        else:
            self.b_axis_current_pos = temporary_rotation