#!/usr/bin/python
'''homework3'''
# pylint: disable= invalid-name
# pylint: disable= too-few-public-methods
import time
import json
import psutil
import config


class Printoto:
    '''docstring for Printoto'''

    def __init__(self):
        self.a = None

    def v(self, l):
        '''h3'''
        self.a = 0
        if config.format_p == 'txt':
            f = open("log.txt", "w")
            for i in l:
                f.write("%s\n" % i)
        else:
            f = open("log.json", "w")
            wj = json.dumps(l)
            f.write(wj)


t_st = ['time']
mem_info = ['memory']
d_usage = ['du']
cpu_info = ['cpu']
swap_info = ['swap']
net_info = ['net']
io_info = ['io']


def timer_monitor():
    '''h3'''
    while True:
        time.sleep(config.time_step)
        mi = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        swap = psutil.swap_memory().used
        io = psutil.net_io_counters(pernic=False)
        di = []
        for dp in psutil.disk_partitions():
            try:
                du = psutil.disk_usage(dp.mountpoint)
            except Exception:  # pylint: disable= broad-except
                continue
            di.append(round(du.free / 1024 / 1024 / 1024, 2))
        t_st.append(time.strftime("%H:%M:%S %d-%m-%Y"))
        mem_info.append(round(mi.available / 1024 / 1024 / 1024, 2))
        d_usage.append(di)
        cpu_info.append(cpu)
        swap_info.append(round(swap / 1024 / 1024 / 1024, 4))
        io_info.append(round(io.bytes_sent / 1024 / 1024 / 1024, 2))
        snapshot = (t_st, d_usage, mem_info, cpu_info, swap_info, io_info)
        if mem_info.__len__() >= config.size_count:
            mem_info.pop(1)
            d_usage.pop(1)
            cpu_info.pop(1)
            io_info.pop(1)
            t_st.pop(1)
            swap_info.pop(1)
        monitor = Printoto()
        monitor.v(snapshot)


timer_monitor()

