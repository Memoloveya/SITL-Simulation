import subprocess
import threading


# 定义一个函数来运行命令
def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()

# /usr/local/bin/

# 命令列表
commands = [
    "dronekit-sitl copter --home=5.147099,100.493824,0,180",
    "dronekit-sitl copter -I1 --home=5.147036,100.493809,0,180",

    "mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:172.17.192.1:14551",
    "mavproxy.py --master tcp:127.0.0.1:5770 --out udp:127.0.0.1:14552 --out udp:172.17.192.1:14552",

]

# 创建线程并运行命令
threads = [threading.Thread(target=run_command, args=(command,)) for command in commands]

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()
