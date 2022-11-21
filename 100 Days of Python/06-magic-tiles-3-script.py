from pynput.mouse import Controller, Button, Listener
from mss import mss

# def on_click(x, y, button, pressed):
#     if pressed:
#         print('mouse click at ({0},{1})'.format(x, y))

# with Listener(on_click=on_click) as listener:
#     listener.join()

# on_click()


def tile_bot():
    x_coord = 1401
    y_coord = 697
    screenshot = (x_coord, y_coord, x_coord + 404, y_coord + 51)
    middle_tile = (51, 152, 253, 354)
    mouse = Controller()
    with mss() as sct:
        img = sct.grab(screenshot)
        for mid in middle_tile:
            if img.pixel(mid, 0)[0] == 0 and img.pixel(mid, 6)[0] == 0:
                mouse.position = (x_coord + mid, y_coord + 70)
                mouse.click(Button.left, 1)

                print(f"Clicked at {mouse.position}")


while True:
    tile_bot()