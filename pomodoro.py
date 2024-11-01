from sense_hat import SenseHat
import time
sense = SenseHat()

def alert(color):
    sense.clear()

    time.sleep(1)

    # Inner level

    sense.set_pixel(3,3, color)
    sense.set_pixel(3,4, color)
    sense.set_pixel(4,3, color)
    sense.set_pixel(4,4, color)

    time.sleep(1)

    # Second level

    sense.set_pixel(2,2, color)
    sense.set_pixel(2,3, color)
    sense.set_pixel(2,4, color)
    sense.set_pixel(2,5, color)

    sense.set_pixel(3,2, color)
    sense.set_pixel(3,5, color)

    sense.set_pixel(4,2, color)
    sense.set_pixel(4,5, color)

    sense.set_pixel(5,2, color)
    sense.set_pixel(5,3, color)
    sense.set_pixel(5,4, color)
    sense.set_pixel(5,5, color)

    time.sleep(1)

    # Third level

    sense.set_pixel(1,1, color)
    sense.set_pixel(1,2, color)
    sense.set_pixel(1,3, color)
    sense.set_pixel(1,4, color)
    sense.set_pixel(1,5, color)
    sense.set_pixel(1,6, color)

    sense.set_pixel(2,1, color)
    sense.set_pixel(3,1, color)
    sense.set_pixel(4,1, color)
    sense.set_pixel(5,1, color)

    sense.set_pixel(2,6, color)
    sense.set_pixel(3,6, color)
    sense.set_pixel(4,6, color)
    sense.set_pixel(5,6, color)

    sense.set_pixel(6,1, color)
    sense.set_pixel(6,2, color)
    sense.set_pixel(6,3, color)
    sense.set_pixel(6,4, color)
    sense.set_pixel(6,5, color)
    sense.set_pixel(6,6, color)

    time.sleep(1)

    # Outer level


    sense.set_pixel(0,0, color)
    sense.set_pixel(0,1, color)
    sense.set_pixel(0,2, color)
    sense.set_pixel(0,3, color)
    sense.set_pixel(0,4, color)
    sense.set_pixel(0,5, color)
    sense.set_pixel(0,6, color)
    sense.set_pixel(0,7, color)

    sense.set_pixel(1,0, color)
    sense.set_pixel(2,0, color)
    sense.set_pixel(3,0, color)
    sense.set_pixel(4,0, color)
    sense.set_pixel(5,0, color)
    sense.set_pixel(6,0, color)

    sense.set_pixel(1,7, color)
    sense.set_pixel(2,7, color)
    sense.set_pixel(3,7, color)
    sense.set_pixel(4,7, color)
    sense.set_pixel(5,7, color)
    sense.set_pixel(6,7, color)

    sense.set_pixel(7,0, color)
    sense.set_pixel(7,1, color)
    sense.set_pixel(7,2, color)
    sense.set_pixel(7,3, color)
    sense.set_pixel(7,4, color)
    sense.set_pixel(7,5, color)
    sense.set_pixel(7,6, color)
    sense.set_pixel(7,7, color)

    time.sleep(1)


while True:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    alert(RED)
    alert(GREEN)
    alert(BLUE)
