#!/bin/bash
systemctl --user stop unit365.service
systemctl --user disable unit365.service
rm ~/.config/systemd/user/unit365.service
systemctl --user daemon-reload
sudo rm -rf /opt/Unit365
