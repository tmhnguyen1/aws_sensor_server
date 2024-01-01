#!/bin/bash

echo "$(date) Log convert entry" >> /app/data/convertlog.log
python3 /app/data_convert.py