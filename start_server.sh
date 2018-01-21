#!/bin/bash -e

cd /projects/pennapps
gunicorn -w 4 -k gevent -b unix:/tmp/pennapps.sock -m 005 app:app --daemon &> /dev/null
