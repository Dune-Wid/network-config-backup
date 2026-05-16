# Automated Network Configuration Backup System

## 📌 Project Overview
This project is a Python-based automation tool designed to securely connect to Cisco enterprise routers, retrieve their running configurations, and automatically archive them locally with timestamped filenames. 

This script eliminates the need for manual SSH sessions and ensures that network configurations are consistently backed up for disaster recovery and auditing purposes.

## 🛠️ Technology Stack
* **Language:** Python 3
* **Libraries:** `netmiko`, `datetime`
* **Target Environment:** Cisco IOS XE (Catalyst 8000v) via Cisco DevNet
* **Protocols:** SSHv2

## 🚀 How It Works
1. **Secure Connection:** Uses Netmiko's `ConnectHandler` to establish an SSH connection to the target Cisco device.
2. **Data Extraction:** Executes the `show running-config` command in privilege exec mode.
3. **Automated Archiving:** Captures the output and dynamically generates a `.txt` file named with the current date and time (e.g., `Router_Backup_2026-05-16_13-30-00.txt`).
4. **Error Handling:** Includes `try/except` blocks to gracefully handle connection timeouts or authentication failures.

## 💻 Example Output
```text
Attempting to connect to the router...
Successfully connected!
Pulling running configuration. This might take a few seconds...

SUCCESS! Configuration saved to: Router_Backup_2026-05-16_13-30-00.txt