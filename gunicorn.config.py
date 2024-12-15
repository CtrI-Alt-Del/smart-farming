# -*- coding: utf-8 -*-

import multiprocessing

chdir = "src/app"

bind = "0.0.0.0:8000"
backlog = 2048

# Log level
loglevel = "info"

# Log to stderr. Defaults to os.isatty.
logfile = None

# Redirect output to a file
accesslog = "-"

# Redirect error log to a file
errorlog = "-"

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = 1000

daemon = False
timeout = 300
keepalive = 2
