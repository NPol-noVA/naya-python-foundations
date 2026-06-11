def check(r, c, seat):
    if seat[r][c] == 'O':
        return True
    else:
        return False


def loadsample(seat):
    sample = [
        ['O', 'R', 'O', 'R', 'R'],
        ['R', 'O', 'R', 'O', 'R'],
        ['O', 'O', 'O', 'R', 'R'],
        ['R', 'R', 'O', 'O', 'O'],
        ['O', 'O', 'R', 'R', 'R']
    ]

    for r in range(5):
        for c in range(5):
            seat[r][c] = sample[r][c]


def reset(seat):
    for r in range(5):
        for c in range(5):
            seat[r][c] = 'O'

    print("The map has been reset")


def reserve(seat):
    r = int(input("Select the row for your seat (0-4): "))
    c = int(input("Select the column for your seat (0-4): "))

    if r < 0 or r >= 5 or c < 0 or c >= 5:
        print("There is no such seat")

    elif check(r, c, seat):
        seat[r][c] = 'R'
        print("You have reserved it successfully")

    else:
        print("Sorry, this seat has already been occupied")


def cancel(seat):
    r = int(input("Select the row for your seat (0-4): "))
    c = int(input("Select the column for your seat (0-4): "))

    if r < 0 or r >= 5 or c < 0 or c >= 5:
        print("There is no such seat")

    elif seat[r][c] == 'R':
        seat[r][c] = 'O'
        print("You have canceled the reservation successfully")

    else:
        print("This seat is not reserved")


def kadjacent(seat, n):
    for r in range(5):

        count = 0

        for c in range(5):
            if seat[r][c] == 'O':
                count += 1

                if count == n:
                    return r, c - n + 1, True

            else:
                count = 0

    return -1, -1, False


def statics(seat):
    for r in range(5):
        reserved = 0

        for c in range(5):
            if seat[r][c] == 'R':
                reserved += 1

        free = 5 - reserved
        percentage = (reserved / 5) * 100

        print(
            "The row {} has {} reserved seats and {} free seats."
            .format(r, reserved, free)
        )

        print(
            "The percentage of occupancy in this row is {}%"
            .format(percentage)
        )


def printer(seat):
    print("\nSeat Map:")

    print("   0 1 2 3 4")

    for r in range(5):
        print(r, end="  ")

        for c in range(5):
            print(seat[r][c], end=" ")

        print()


def showthelist():
    print("\nOptions:")
    print("1 - Load a seat sample")
    print("2 - Reset the map")
    print("4 - Reserve a seat")
    print("5 - Cancel reservation")
    print("7 - Locate k adjacent seats in a row")
    print("8 - See statistics")
    print("9 - See the map")
    print("0 - Exit")


# Main program

seat = [
    ['O', 'R', 'O', 'R', 'R'],
    ['R', 'O', 'R', 'O', 'R'],
    ['O', 'O', 'O', 'R', 'R'],
    ['R', 'R', 'O', 'O', 'O'],
    ['O', 'O', 'R', 'R', 'R']
]


z = 14

while z == 14:

    print("\nWelcome! If you want to see the options enter 1")

    x = int(input())

    if x == 1:
        showthelist()

    else:
        break

    x = int(input())

    if x == 0:
        break

    if x == 1:
        loadsample(seat)

    elif x == 2:
        reset(seat)

    elif x == 4:
        reserve(seat)

    elif x == 5:
        cancel(seat)

    elif x == 7:
        k = int(input("Enter the number of seats you want to locate: "))

        nrow, ncol, v = kadjacent(seat, k)

        if v:
            print(
                "The first available seats start at row {} and column {}"
                .format(nrow, ncol)
            )
        else:
            print("No available adjacent seats found")

    elif x == 8:
        statics(seat)

    elif x == 9:
        printer(seat)

    print("\nIf you want to make another operation enter 14")
    z = int(input())