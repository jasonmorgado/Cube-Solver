from rubik_solver import utils
# https://github.com/Wiston999/python-rubik


def display_cube(cube_state):
    """Takes cube string as input, prints formatted cube"""
    row_size = 3
    cube_rows = []
    for i in range(0, len(cube_state), row_size):
        cube_rows.append(cube_state[i:i+row_size])
    # Top Face
    for row in cube_rows[:3]:
        print("      {} {} {}".format(row[0], row[1], row[2]))
    # Middle sides
    top_row = cube_rows[3] + cube_rows[6] + cube_rows[9] + cube_rows[12]
    middle_row = cube_rows[4] + cube_rows[7] + cube_rows[10] + cube_rows[13]
    bottom_row = cube_rows[5] + cube_rows[8] + cube_rows[11] + cube_rows[14]
    for row in [top_row, middle_row, bottom_row]:
        for character in row:
            print(character, end=' ')  # no newline
        print("")  # Newline
    # Bottom
    for row in cube_rows[-3:]:
        print("      {} {} {}".format(row[0], row[1], row[2]))


def fetch_state():
    """
    Prompts the user for input from all sides
    Reads all sides as rotated directly from front face
    Red is front, Yellow is top
    """
    sides = "Yellow", "Blue", "Red", "Green", "Orange", "White"
    cube_state = ""
    for side in sides:
        side_string = input("Input colors for the {} Face:".format(side))
        cube_state = cube_state + side_string.lower()
    return cube_state


def solve(cube_state):
    """
    Takes a string representing the current cube
    Returns the solution as a list of strings
    """
    solution = utils.solve(cube_state, "Kociemba")
    print(solution)
    return solution


def main():
    # Fetch cube state
    # cube_state = fetch_state()
    # OpenCV stuff would go here
    cube_state = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
    display_cube(cube_state)

    # Generate Solution
    solution = solve(cube_state)
    print(solution)

    # Send to Arduino would go here


if __name__ == '__main__':
    main()
