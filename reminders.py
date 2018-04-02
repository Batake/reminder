# coding:utf-8

from subprocess import Popen, PIPE

script_org = \
'''
on run argv

    set pylist to "Python Notification"

    tell application "Reminders"
        set notification to make new reminder in list pylist
        set name of notification to "{0}"
        set body of notification to "{1}"
        set remind me date of notification to (current date) + ({2} * minutes)
    end tell

end run
'''

def notify(title, message, delay):
    script_send = script_org.format(title, message, delay)
    command = Popen(['osascript'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    command.communicate(script_send)


if __name__ == '__main__':
    notify()
