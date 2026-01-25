# Unit365 (Keyboard Logger Service)

> Unit365 is a tactical keyboard monitor running in the background, saving keystrokes to a safe location.

---

## Installation

1. Clone or copy the repository:

```bash
git clone https://github.com/cyb2rS2c/Unit365.git Unit365
cd Unit365
````

2. Run the deploy script:

```bash
chmod +x deploy.sh;./deploy.sh
```

This will:

* Copy the repository to `/opt/Unit365`
* Create a Python virtual environment
* Install required Python packages from `requirements.txt`
* Set up and start a systemd user service

---

## Log File Location

Logs are stored in:

```
~/.local/share/Unit365/unit365.log
```

This ensures the service runs without requiring root privileges.

---

## Service Management

Check status:

```bash
systemctl --user status unit365.service
```

Stop the service:

```bash
systemctl --user stop unit365.service
```

Restart the service:

```bash
systemctl --user restart unit365.service
```

Remove the service:

```bash
chmod +x uninstall.sh;./uninstall.sh
```

---
## Author
cyb2rS2c - [GitHub Profile](https://github.com/cyb2rS2c)

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer!

This code is provided "as-is" without any warranty. The author is not responsible for any misuse or damage caused by the use of this software. Always practice responsible security testing.
