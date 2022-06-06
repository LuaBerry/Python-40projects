import psutil

cur_sent = 0
cur_recv = 0
prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval = 1)
    print(f'CPU usage: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024 ** 3, 1)
    print(f'Available memory: {memory_avail}GB')

    net = psutil.net_io_counters()
    cur_sent = net.bytes_sent / 1024 ** 2
    cur_recv = net.bytes_recv / 1024 ** 2

    sent = round(cur_sent - prev_sent, 1)
    recv = round(cur_recv - prev_recv, 1)

    print(f'Sent: {sent}MB Received: {recv}MB')

    prev_sent = cur_sent
    prev_recv = cur_recv