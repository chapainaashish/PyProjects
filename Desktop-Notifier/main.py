# Send Desktop Notification
# Used my own package :D
# https://pypi.org/project/notifylinux

from notifylinux.linuxnotifier import Notifier

notify = Notifier(title="Hello Aashish", descriptions="Welcome to Linux",
                  iconpath="/home/aashishsharma/Documents/Python Journey/Python Projects/Desktop Notifier/icon/help-about.svg", timeout=5, urgency="normal")
notify.send_notification()
