import curses
from time import sleep

blink_half_period = 1 / 6
blink_reps = 3 * 4 * 4
total_time = 25 * 60

def main(stdscr):
    stdscr.clear()
    while total_time > 0:
        secs = total_time % 60
        mins = int(total_time / 60.0)
        if secs < 10:
            secs = '0' + str(secs)
        if mins < 10:
            mins = '0' + str(mins)
        stdscr.addstr(1, 0, '0:{}:{}'.format(mins, secs))
        stdscr.refresh()
        total_time -= 1
        sleep(1)
    for i in range(blink_reps):
        for row in range(1, 21, 2):
            stdscr.addstr(row, 0, 'DONE '*14, curses.A_REVERSE)
            stdscr.refresh()
        sleep(blink_half_period)
        for row in range(1, 21, 2):
            stdscr.addstr(row, 0, '     '*14)
            stdscr.refresh()
        sleep(blink_half_period)
    stdscr.addstr(1, 0, 'Any key to quit...')
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
