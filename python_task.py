import platform
import os
import speedtest
import psutil
import socket
import platform
import cpuinfo
import uuid
from screeninfo import get_monitors

def get_installed_software():
    # Fetch the list of installed software
    software_list = os.popen('wmic product get name,version').read()
    return software_list

def get_internet_speed():
    # Fetch the internet speed
    st = speedtest.Speedtest()
    download_speed = st.download() / 1e6  # in Mbps
    upload_speed = st.upload() / 1e6  # in Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    # Fetch screen resolution
    monitors = get_monitors()
    resolutions = [(monitor.width, monitor.height) for monitor in monitors]
    return resolutions

def get_cpu_info():
    # Fetch CPU information
    cpu_info = cpuinfo.get_cpu_info()
    cpu_model = cpu_info['brand_raw']
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return cpu_model, cores, threads

def get_gpu_info():
    # Fetch GPU information
    # Note: This may not work on all systems or may require additional libraries
    try:
        import GPUtil
        gpu_list = GPUtil.getGPUs()
        if gpu_list:
            gpu_model = gpu_list[0].name
        else:
            gpu_model = "N/A"
    except ImportError:
        gpu_model = "N/A"
    return gpu_model

def get_ram_size():
    # Fetch RAM size
    ram_size = psutil.virtual_memory().total / (1024 ** 3)  # in GB
    return ram_size

def get_screen_size():
    # Fetch screen size
    # Note: This may not be accurate for all systems
    # You might need to adjust this based on the actual display size
    return "15 inch"

def get_mac_address():
    # Fetch MAC address
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return mac_address


def get_public_ip():
    # Fetch public IP address
    public_ip = socket.gethostbyname(socket.gethostname())
    return public_ip

def get_windows_version():
    # Fetch Windows version
    windows_version = platform.platform()
    return windows_version

if __name__ == "__main__":
    print("1. Installed Software List:")
    print(get_installed_software())

    print("\n2. Internet Speed:")
    download_speed, upload_speed = get_internet_speed()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

    print("\n3. Screen Resolution:")
    resolutions = get_screen_resolution()
    for i, resolution in enumerate(resolutions, start=1):
        print(f"Monitor {i}: {resolution[0]}x{resolution[1]} pixels")

    print("\n4. CPU Information:")
    cpu_model, cores, threads = get_cpu_info()
    print(f"Model: {cpu_model}")
    print(f"Number of Cores: {cores}")
    print(f"Number of Threads: {threads}")

    print("\n5. GPU Information:")
    gpu_model = get_gpu_info()
    print(f"Model: {gpu_model}")

    print("\n6. RAM Size:")
    ram_size = get_ram_size()
    print(f"Size: {ram_size:.2f} GB")

    print("\n7. Screen Size:")
    screen_size = get_screen_size()
    print(f"Size: {screen_size}")

    print("\n8. WiFi/Ethernet MAC Address:")
    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")

    print("\n9. Public IP Address:")
    public_ip = get_public_ip()
    print(f"Public IP: {public_ip}")

    print("\n10. Windows Version:")
    windows_version = get_windows_version()
    print(f"Version: {windows_version}")
