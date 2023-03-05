import tkinter as tk
import time
import signal

def increment_count():
    global count
    count += 1
    time.sleep(0.05)
    count_label.config(text=f"Count: {count}")

def decrement_count():
    global count
    count -= 1
    time.sleep(0.05)
    count_label.config(text=f"Count: {count}")

def auto_decrement():
    global count
    count -= 1
    
    count_label.config(text=f"Count: {count}")
    if count <= 0:
        window.destroy()
    else:
        window.after(1000, auto_decrement)
        time.sleep(0.05)

def handle_signal(sig, frame):
    window.destroy()
    exit()

count = 0
window = tk.Tk()
window.title("Counting Program")
count_label = tk.Label(window, text=f"Count: {count}")
count_label.pack()
increment_button = tk.Button(window, text="Increment", command=increment_count)
increment_button.pack()
decrement_button = tk.Button(window, text="Decrement", command=decrement_count)
decrement_button.pack()
auto_decrement_button = tk.Button(window, text="Start Auto-Decrement", command=auto_decrement)
auto_decrement_button.pack()

# Set up signal handler
signal.signal(signal.SIGINT, handle_signal)

window.mainloop()
