import os
import cmd
import shellFunction
import subprocess
import psutil
import msvcrt
import signal
class TinyShell(cmd.Cmd):
    intro = 'Welcome to the Tiny shell.\nType help to list commands.\n'
    prompt = "$TinyShell$ "
    def __init__(self):
        super().__init__()
        self.bg_processes = []

    def do_pwd(self, line):
        """Print the current working directory"""
        print(os.getcwd())
    def do_exists(self,line):
        result = os.path.exists(line) 
        print(result)
    def do_size(self,line):
        size = os.path.getsize(line)
        print("Size of the file is", size," bytes.")
    def do_cd(self, line):
        """Change the current working directory"""
        os.chdir(line)
    def do_check(self, line):
        """Check Process"""
        shellFunction.check_processes(self)
        
    def do_runfg(self, line):
        args = line.split()
        shellFunction.run_foreground(args)
        
    def do_runbg(self, line):
        """Run a command or a script in the background"""
        args = line.split()
        for arg in args:
            arg = f"python {arg}"
            process = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            self.bg_processes.append(process.pid)  # Thêm pid của tiến trình mới vào danh sách
            print(f"Started background process with PID {process.pid}")
            

    def do_killbg(self, line):
        """Kill a background process"""
        args = line.split()
        shellFunction.kill_processbg(self,args)

    def do_stop(self, line):
        """Stop a background process"""
        args = line.split()
        shellFunction.stop_processbg(args)

    def do_resume(self, line):
        """Resume a background process"""
        args = line.split() 
        shellFunction.resume_processbg(args)

    def do_callBat(self, line):
        with open(line, 'r') as f:
            for cmd in f:   
                cmd = cmd.strip()
                self.onecmd(cmd)

    def default(self, line):
        output = os.popen(line).read()
        print(output)

    def do_addPath(self, line):
        """Add a new directory to the PATH environment variable"""
        new_path = line.strip()
        os.environ['PATH'] = os.pathsep.join([new_path, os.environ['PATH']])

    def do_exit(self, line):
        return True

if __name__ == '__main__':
    shell = TinyShell()
    shell.cmdloop()
