#!/bin/bash

REPO_NAME="Unit365"
INSTALL_DIR="/opt/$REPO_NAME"
SERVICE_NAME="unit365.service"
USER_SERVICE_DIR="$HOME/.config/systemd/user"

sudo mkdir -p "$INSTALL_DIR"
sudo cp -r ./* "$INSTALL_DIR/"

if [ ! -d "$INSTALL_DIR/myvenv" ]; then
    sudo python3 -m venv "$INSTALL_DIR/myvenv"
fi

sudo "$INSTALL_DIR/myvenv/bin/pip" install --upgrade pip
sudo "$INSTALL_DIR/myvenv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

mkdir -p "$USER_SERVICE_DIR"

cat > "$USER_SERVICE_DIR/$SERVICE_NAME" <<EOL
[Unit]
Description=Unit365 Keyboard Service
After=graphical.target

[Service]
Type=simple
ExecStart=$INSTALL_DIR/myvenv/bin/python $INSTALL_DIR/unit365.py
Restart=on-failure
Environment=DISPLAY=:0
Environment=XAUTHORITY=$HOME/.Xauthority

[Install]
WantedBy=default.target
EOL

systemctl --user daemon-reload
systemctl --user enable "$SERVICE_NAME"
systemctl --user start "$SERVICE_NAME"

echo "Unit365 installed and service started!"
