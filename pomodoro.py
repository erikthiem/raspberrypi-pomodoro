from sense_hat import SenseHat
import time
sense = SenseHat()

def alert(color):
    O = [0,0,0] # Light turned off
    X = color   # Easy symbol to visually see in code

    f0 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]

    f1 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]

    f2 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]

    f3 = [
        O, O, O, O, O, O, O, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, X, X, X, X, X, X, O,
        O, O, O, O, O, O, O, O
    ]

    f4 = [
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
    ]

    frames = [f0, f1, f2, f3, f4]

    for frame in frames:
        sense.set_pixels(frame)
        time.sleep(1)

# Detect the raspberry pi being picked up.
# Technically detects "shake", but assuming it is sitting still, this will detect somebody picking it up.
def detect_pickup():
    x, y, z = sense.get_accelerometer_raw().values()

    axis_movement_count = 0

    axis_movement_count += abs(x) > 0.5
    axis_movement_count += abs(y) > 0.5
    axis_movement_count += abs(z) > 0.5

    if axis_movement_count >= 2:
        return True

    return False

picked_up = False
while not picked_up:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # alert(RED)
    # alert(GREEN)
    # alert(BLUE)

    picked_up = detect_pickup()
    time.sleep(0.05)

print('picked up')
