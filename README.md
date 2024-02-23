# dsysinfo Version 1.0

System Information Daemon
The System Information Daemon is a Python script that continuously monitors and displays various system information such as hardware details, network information, disk usage, process information, system uptime, logged-in users, file systems, kernel version, and more. It utilizes the psutil, socket, and subprocess modules to gather system-related data and prints them to the console.

Usage
Clone the Repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/system-info-daemon.git
Navigate to Directory: Enter the directory containing the script:

bash
Copy code
cd system-info-daemon
Run the Script: Execute the Python script using the following command:

bash
Copy code
python system_info_daemon.py
View System Information: Once the script is running, it will continuously update and display system information in the console every 10 seconds.

System Information Displayed
Hardware Information: CPU details, RAM size, and serial number (if available).
Network Information: IP address, netmask, and broadcast IP for each network interface.
Disk Usage Information: Total, used, and free space for each disk partition.
Top Processes: List of top processes by CPU usage and memory consumption.
System Uptime: Duration since system boot.
Logged-in Users: List of users currently logged into the system.
File Systems: Information about mounted file systems.
Kernel Version: Version of the Linux kernel running on the system.
Dependencies
Python 3.x
psutil
socket
subprocess
Notes
This script is designed to run on Linux systems.
Ensure that the necessary dependencies are installed before running the script.
The script may require administrative privileges to access certain system information.
