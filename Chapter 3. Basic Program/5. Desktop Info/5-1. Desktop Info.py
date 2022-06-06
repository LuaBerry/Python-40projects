import psutil
import os

def Print_save(list, str):
    print(str)
    list.append(str + "\n")
info_list = []
cpu_freq = psutil.cpu_freq()
cpu_max_ghz = round(cpu_freq.max / 1000, 2)
Print_save(info_list, f"CPU max speed: {cpu_max_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
Print_save(info_list, f"CPU core: {cpu_core}") 

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024 ** 3)
Print_save(info_list, f"Total memory: {memory_total}GB")

disk = psutil.disk_partitions()
for p in disk:
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024 ** 3)
    Print_save(info_list, p.mountpoint + " " + p.fstype + f' Disk Capacity: {disk_total}GB')

net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024 ** 2, 1)
recv = round(net.bytes_recv / 1024 ** 2, 1)
Print_save(info_list, f"Sent: {sent}MB Received: {recv}MB")

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = dir_path + "\\Info.txt"
with open(file_path, 'wt', encoding='UTF-8') as f:
    f.write("Desktop Info \n\n")
    f.writelines(info_list)