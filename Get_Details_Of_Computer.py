

import platform
import psutil
import matplotlib.pyplot as plt
import subprocess
import pyttsx3
engine = pyttsx3.init()
import os
import qrcode
import wmi 
import re
import pyfiglet  # for ascii_art


def sysinfo():
    result = subprocess.check_output(['systeminfo'], universal_newlines=True)
    for line in result.splitlines():
        if line.strip():
            print(line.strip())


def sysinfo1():
        my_system = platform.uname()

        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")
        c = wmi.WMI()   
        my_system = c.Win32_ComputerSystem()[0] 
        print(f"Manufacturer: {my_system.Manufacturer}")
        print(f"Model: {my_system.Model}")
        print(f"Name: {my_system.Name}")
        print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
        print(f"SystemType: {my_system.SystemType}")
        print(f"SystemFamily: {my_system.SystemFamily}")


def sysinfo2():
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 * 1024 * 1024)  # Convert to gigabytes (GB)
    labels = ['Available', 'Used', 'Free']
    sizes = [memory.available, memory.used, memory.free]
    colors = ['#2ecc71', '#e74c3c', '#3498db']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.pie([total_memory, 100 - memory.percent], colors=['white', 'white'], radius=0.6)
    center_circle = plt.Circle((0, 0), 0.4, color='white', linewidth=0)
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.title(f'Memory Usage\nTotal Memory: {total_memory:.2f} GB')
    plt.show()


def genqr1():
    url = input("Enter the URL for the QR code: ")
    img = qrcode.make(url)
    img.save("qrCode.png", "PNG")
    os.system("start qrCode.png")


def hardwareinfo():
    disk_usage = psutil.disk_usage('/')
    total_space = disk_usage.total / (1024 ** 3)
    used_space = disk_usage.used / (1024 ** 3)
    free_space = disk_usage.free / (1024 ** 3)
    percentage_used = disk_usage.percent
    fig, ax = plt.subplots()
    ax.pie([used_space, free_space], radius=1.0, labels=['Used', 'Free'],
        colors=['#e74c3c', '#2ecc71'], autopct='%1.1f%%',
        startangle=90, counterclock=False, wedgeprops=dict(edgecolor='black'))
    ax.set_aspect('equal')
    plt.title(f"Total Disk Space: {total_space:.2f} GB")
    plt.show()


def allhrd():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    labels = ['CPU', 'RAM', 'Disk']
    sizes = [cpu_usage, ram_usage, disk_usage]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('*Hardware Usage*')
    plt.show()


def allprocesses():
    running_count = 0
    stopped_count = 0
    for process in psutil.process_iter():
        if process.status() == psutil.STATUS_RUNNING:
            running_count += 1
        elif process.status() == psutil.STATUS_STOPPED:
            stopped_count += 1


    labels = ['Running', 'Stopped']
    counts = [running_count, stopped_count]
    positions = range(len(labels))
    fig, ax = plt.subplots()
    ax.bar(positions, counts, align='center', color=['#1f77b4', '#ff7f0e'])
    for i, count in enumerate(counts):
        ax.text(i, count, str(count), ha='center', va='bottom')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_title('Running and Stopped Processes')
    ax.set_xlabel('Status')
    ax.set_ylabel('Count')
    plt.show()


def list_running_services():
    services = psutil.win_service_iter()
    for service in services:
        print(f"Service Name: {service.name()}")
        print(f"Service Display Name: {service.display_name()}")
        print(f"Service Status: {service.status()}\n")
def stop_service(service_name):
    try:
        service = psutil.win_service_get(service_name)
        service.stop()
        print(f"The {service_name} service has been stopped.")
    except psutil.NoSuchProcess:
        print(f"The {service_name} service does not exist.")
    except psutil.AccessDenied:
        print(f"Access denied to stop {service_name} service. Run the script with administrative privileges.")
def runingandstop():
    list_running_services()
    service_name_to_stop = "MyService"
    stop_service(service_name_to_stop)


def regxnum1(input_string):
    pattern = r'^\+91 [6-9]\d{9}$'
    match = re.match(pattern, input_string)
    return match is not None
def rexnum():
    phone_number = input("Enter an Indian phone number (with country code): ")
    if regxnum1(phone_number):
        print(f"{phone_number} is a valid Indian phone number.")
    else:
        print(f"{phone_number} is not a valid Indian phone number.")


def validate_email(email):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@techgenies\.com$'
    match = re.match(pattern, email)
    return match is not None
def check_email():
    email = input("Enter your organization's email: ")
    if validate_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is not a valid email.")



def handle_option_default():
    if option == '0':
        exit()
    else:
        print("Invalid option selected")



name = input("What's your name? ")
ascii_art = pyfiglet.figlet_format(name)
print(ascii_art)
engine.say(f"Hello, Mr {name}")
engine.say("Hope you are doing well")
engine.say(f"These are the option below you can choose")
engine.runAndWait()


print()
while True:        
    option = input( "1> all systeminfo\n"
                    "2> few system options\n" 
                    "3> Show Memory Usage In Graph\n"
                    "4> Create QR code for any usage\n"
                    "5> Hardware Informations in Graph\n"
                    "6> See Disk, Hardware, or memory usage in Graph\n"
                    "7> Number of process show in Graph\n"
                    "8> Runing and stop process with details\n"
                    "9> Check Indian phone number\n"
                    "10> Check your organization's email\n"
                    "0> Exit\n"
                    "Enter your choice: ")


    option_handlers = {
        "1": sysinfo,
        "2": sysinfo1,
        "3": sysinfo2,
        "4": genqr1,
        "5": hardwareinfo,
        "6": allhrd,
        "7": allprocesses,
        "8": runingandstop,
        "9": rexnum,
        "10": check_email,
    }

    option_handlers.get(option, handle_option_default)()
    print()













