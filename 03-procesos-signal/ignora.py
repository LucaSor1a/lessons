import os
import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGKILL, signal.SIG_IGN)
print os.getpid()
leido = raw_input()

print leido
