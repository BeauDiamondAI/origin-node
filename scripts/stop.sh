#!/bin/bash
# stop.sh — remove the wake cron job. Run this if you (Beau) want to pause
# the project. Re-install with: crontab /home/ec2-user/origin-node/scripts/cron.txt
crontab -l > /home/ec2-user/origin-node/scripts/cron.txt.bak 2>/dev/null
crontab -r 2>/dev/null && echo "wake cron removed (backup saved to scripts/cron.txt.bak)"
