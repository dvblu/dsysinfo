import os
import time
import platform
import psutil
import socket
import subprocess


class SystemInfoDaemon:
    def __init__(self):
        pass

    def fetch_system_info(self):
        try:
            print("\033[95mUpdating system information...\033[0m")
            print("-" * 50)
            self.print_hardware_info()
            self.print_network_info()
            self.print_disk_usage()
            self.print_process_info()
            self.print_system_uptime()
            self.print_logged_in_users()
            self.print_file_systems()
            self.print_kernel_version()
            print("\033[95mSystem information updated\033[0m")
        except Exception as e:
            print(f"\033[91mError fetching system information: {e}\033[0m")

    def print_disk_usage(self):
        print("\n\033[96mDisk Usage Information:\033[0m")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"Partition: {partition.mountpoint}")
            print(f"  Total: {usage.total / (1024 ** 3):.2f} GB")
            print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
            print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
            print("-" * 50)

    def print_process_info(self):
        print("\n\033[96mTop Processes:\033[0m")
        try:
            processes = sorted(psutil.process_iter(), key=lambda p: p.cpu_percent(), reverse=True)[:5]
            for process in processes:
                print(f"PID: {process.pid}, CPU: {process.cpu_percent()}%, Memory: {process.memory_info().rss / (1024 ** 2):.2f} MB")
        except Exception as e:
            print(f"Error fetching process information: {e}")

    def print_system_uptime(self):
        print("\n\033[96mSystem Uptime:\033[0m")
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        print(f"{uptime_str}")

    def print_logged_in_users(self):
        print("\n\033[96mLogged-in Users:\033[0m")
        logged_in_users = subprocess.check_output(["who"]).decode("utf-8")
        print(logged_in_users)

    def print_file_systems(self):
        print("\n\033[96mFile Systems:\033[0m")
        df_output = subprocess.check_output(["df", "-h"]).decode("utf-8")
        print(df_output)

    def print_kernel_version(self):
        print("\n\033[96mKernel Version:\033[0m")
        kernel_version = subprocess.check_output(["uname", "-r"]).decode("utf-8").strip()
        print(kernel_version)

    def print_hardware_info(self):
        print("\n\033[96mHardware Information:\033[0m")
        print("-" * 50)
        cpu_info = f"CPU: {platform.processor()}"
        print(cpu_info)
        ram_info = f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        print(ram_info)
        serial_number = self.get_serial_number()
        if serial_number:
            print(f"Serial Number: {serial_number}")
        else:
            print("Serial Number: Not available")
        print("-" * 50)

    def get_serial_number(self):
        try:
            # Attempt to read the serial number from a file or another source
            # If successful, return the serial number
            # If unsuccessful, raise an exception or return None
            return "SerialNumber123"  # Hardcoded serial number
        except Exception as e:
            print(f"Error fetching serial number: {e}")
            return None

    def print_network_info(self):
        print("\n\033[96mNetwork Information:\033[0m")
        interfaces = psutil.net_if_addrs()
        for iface, addrs in interfaces.items():
            if iface.startswith("e") or iface.startswith("w"):
                print("-" * 50)
                print(f"Network Interface: {iface}")
                for address in addrs:
                    if address.family == socket.AF_INET:
                        print(f"  IP Address: {address.address}")
                        print(f"  Netmask: {address.netmask}")
                        print(f"  Broadcast IP: {address.broadcast}")
                print("-" * 50)
                break

    def update_system_info(self):
        while True:
            self.print_pid()
            self.fetch_system_info()
            time.sleep(10)

    def print_pid(self):
        print(f"\n\033[96mDaemon PID: {os.getpid()}\033[0m")


def run_daemon():
    daemon_obj = SystemInfoDaemon()
    print("\033[95mRunning daemon...\033[0m")
    daemon_obj.update_system_info()


if __name__ == "__main__":
    run_daemon()

