# Python Packet Sniffer

This Python script is a simple console-based network packet sniffer built using the `scapy` library. It allows users to configure network settings, capture network packets, and save them to a file for later analysis.

## Features

- **Settings Menu**: Configure network interface, packet filter, save file, and local port.
- **Packet Capture**: Capture and display network packets in real-time.
- **Save Packets**: Save captured packets to a specified file.

## Requirements

- Python 3.x
- `scapy` library

To install the `scapy` library, use pip:
```sh
pip install scapy
```
# Usage
## Run the Script:

```sh
python main.py
```
## Main Menu:

1. **Settings**: Configure network settings.
2. **Start Capture**: Start capturing packets based on the configured settings.
q. **Quit**: Exit the script.

## Settings Menu:

1. **Network Interface**: Enter the name of the network interface.
2. **Filter**: Enter the filter expression (e.g., tcp, udp).
3. **Save File**: Enter the file path to save captured packets.
4. **Local Port**: Enter the local port to listen on.
5. **List Available Interfaces**: Display a list of available network interfaces.
b. **Back to Main Menu**: Return to the main menu.
Start Capture:

The script will display captured packets in real-time.
Press Ctrl+C to stop capturing and save the packets to the specified file.
Example
1. **Run the script**:

```sh
python main.py
```
2. **In the main menu, select 1 to enter the settings menu.**


3. **In the settings menu**:
- Select 5 to list available network interfaces.
- Choose a valid network interface and set it using option 1.
- Set other options as needed (filter, save file, local port).
4. **Return to the main menu and select 2 to start capturing packets.**


5. **View captured packets in real-time and press Ctrl+C to stop capturing.**

## Terms of Use

- This software is provided "as is" and without any warranty. **The author is not responsible for any misuse or damage caused by this software.** Users must ensure they have the necessary permissions to capture network packets on their systems and are responsible for complying with all applicable laws and regulations.

- By using this software, you agree to use it responsibly and only for lawful purposes. Unauthorized network monitoring and packet capturing may violate local, state, and federal laws. The author disclaims all liability for any actions taken by users of this software.



