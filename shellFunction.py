import subprocess
import msvcrt
import sys
import os
import psutil
#Chạy tuần tự tiến trình
def run_foreground(args):
    for arg in args:
        arg = ".\\" + arg
        p = subprocess.Popen([sys.executable, arg], shell=True)

        # Wait for the process to finish or for CTRL-C to be pressed
        try:
            while p.poll() is None:
                if msvcrt.kbhit() and ord(msvcrt.getch()) == 3:
                    # CTRL-C was pressed, kill the process
                    p.kill()
                    break
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Stopping process...")
            p.kill()
#kiểm tra trạng thái các tiến trình
def check_processes(self):
    print("List of running processes:")
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'status'])
            if process_info['pid'] in self.bg_processes:
                print(f"pid: {process_info['pid']}, name: {process_info['name']}, status: {process_info['status']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
#Kill 1 hay nhiều tiến trình
def kill_processbg(self,args):
    for arg in args:
        pid = int(arg)
        try:
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
            print(f"Background process with PID {pid} has been kill.")
            self.bg_processes.remove(pid)
        except subprocess.CalledProcessError:
            print(f"Failed to kill background process with PID {pid}.")
#Tạm dừng một tiến trình
def stop_processbg(args):
    for arg in args:
        pid = int(arg)
        try:
            p = psutil.Process(pid)
            p.suspend()
            print(f"Process {pid} has been stop.")
        except psutil.NoSuchProcess:
            print(f"No such process with PID {pid}")

#Tiếp tục một hoặc nhiều tiến trình
def resume_processbg(args):
    for arg in args:
        pid = int(arg)
        try:
            p = psutil.Process(pid)
            p.resume()
            print(f"Background process with PID {pid} has been resumed.")
        except psutil.NoSuchProcess:
            print(f"No such process with PID {pid}")

# lấy danh sách tất cả các tiến trình con của một tiến trình với pid cho trước

