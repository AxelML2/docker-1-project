#!/bin/bash
set -e
exec python3 process-data.py &
exec python3 app.py