# Requirements and Network Interfaces for Network Packet Analyzer

## Requirements

- Python 3.x
- Scapy library
- Tkinter library (included with Python standard library)
- WinPcap or Npcap for Windows (for packet capturing)

## Software Requirements

1. **Python**
   - Version: 3.6 or higher
   - [Download Python](https://www.python.org/downloads/)

2. **Required Python Libraries**
   - **Scapy**: A powerful Python library used for network packet manipulation and analysis.
     - Installation: Use the following command to install Scapy via pip:
       ```bash
       pip install scapy
       ```

3. **Operating System Compatibility**
   - **Windows**: The script is compatible with Windows 10 and later.
   - **macOS**: Compatible with macOS 10.15 (Catalina) and later.
   - **Linux**: Compatible with major distributions such as Ubuntu, Fedora, and CentOS.

## Hardware Requirements

- **Network Interface Card (NIC)**: A functional network interface card capable of packet capturing.
- **Network Access**: Ensure you have proper access to the network you intend to analyze.

# Network Interface

The network interface is required to capture network packets. You must specify the correct network interface name when running the script. The following are common interface names:

- **Windows**: 
  - Ethernet, Wi-Fi (e.g., `Ethernet`, `Wi-Fi`)
- **macOS**: 
  - Wi-Fi, Ethernet (e.g., `en0`, `en1`)
- **Linux**: 
  - Ethernet, Wi-Fi (e.g., `eth0`, `wlan0`)


## Common Network Interfaces

### Windows

On Windows systems, network interfaces are typically named with prefixes like `Ethernet`, `Wi-Fi`, or `Local Area Connection`. You can find the names of available network interfaces using the following command in Command Prompt or PowerShell:

```bash
ipconfig
```

*Examples:*
- Ethernet
- Wi-Fi
- Local Area Connection
- vEthernet (Default Switch)

### macOS
On macOS systems, network interfaces can be found using the ifconfig command in Terminal. Interface names usually start with en, awdl, or bridge.

*Examples:*
- en0 (typically the primary Ethernet or Wi-Fi interface)
- en1 (secondary Ethernet or Wi-Fi interface)
- awdl0 (Apple Wireless Direct Link)

### Linux
On Linux systems, network interfaces are named with prefixes like eth, wlan, en, or br. You can list available interfaces using the following command in Terminal:
```bash
ip a
```

*Examples:*
- eth0 (Ethernet interface)
- wlan0 (Wi-Fi interface)
- enp0s3 (another Ethernet interface naming convention)
- lo (loopback interface)

## Finding Your Network Interface
To identify the correct network interface on your system:

1. Windows:
- Open Command Prompt or PowerShell.
- Run `ipconfig` and look for the network adapter you want to use.

2. macOS:
- Open Terminal.
- Run `ifconfig` and look for the interface names.

3. Linux:
- Open Terminal.
- Run `ip a` or ifconfig and look for the interface names.
Make sure to enter the exact name of the network interface into the Network Packet Analyzer program to ensure accurate packet capturing.

#### Thankyou!