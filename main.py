import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import threading
import tkinter
import psutil

root = tkinter.Tk()
root.geometry('1000x620')
root.title("systems info")


def cpu_usage1():
    cpu = psutil.cpu_percent()
    if cpu > 80:
        cpu_usage.configure(bootstyle='danger')
        cpu_usage.configure(amountused=cpu)
        cpu_usage.after(1000, cpu_usage1)
    elif cpu < 80:
        cpu_usage.configure(bootstyle='primary')
        cpu_usage.configure(amountused=cpu)
        cpu_usage.after(1000, cpu_usage1)


def memory_usage1():
    memory = psutil.virtual_memory().percent
    if memory > 50:
        memory_usage.configure(bootstyle="warning")
        memory_usage.configure(amountused=memory)
        memory_usage.after(1000, memory_usage1)
    elif memory < 50:
        memory_usage.configure(bootstyle="primary")
        memory_usage.configure(amountused=memory)
        memory_usage.after(1000, memory_usage1)
    elif memory > 80:
        memory_usage.configure(bootstyle="danger")
        memory_usage.configure(amountused=memory)
        memory_usage.after(1000, memory_usage1)


def stockage_usage1():
    stockage = psutil.disk_usage('/').percent
    if stockage < 20:
        stockage_usage.configure(bootstyle="danger")
        stockage_usage.configure(amountused=stockage)
        stockage_usage.after(1000, stockage_usage1)
    elif stockage < 50:
        stockage_usage.configure(bootstyle="warning")
        stockage_usage.configure(amountused=stockage)
        stockage_usage.after(1000, stockage_usage1)
    elif stockage < 80:
        stockage_usage.configure(bootstyle="primary")
        stockage_usage.configure(amountused=stockage)
        stockage_usage.after(1000, stockage_usage1)


def network():
    notification1 = ToastNotification(
        title="Network info",
        message="OFFLINE",
        duration=3000,
        alert=True
    )
    notification2 = ToastNotification(
        title="Network info",
        message="ONLINE",
        duration=3000
    )

    net_stats1 = psutil.net_io_counters()
    r = net_stats1.bytes_recv
    if r > 0:
        notification2.show_toast()
    else:
        notification1.show_toast()


cpu_usage = ttk.Meter(master=root, metersize=200, subtext="cpu usage", textright='%')
cpu_usage.place(x=150, y=200)
memory_usage = ttk.Meter(master=root, metersize=200, subtext="memory used", textright='%')
memory_usage.place(x=400, y=200)
stockage_usage = ttk.Meter(master=root, metersize=200, amountused=25, subtext="Stockage restant",
                           stripethickness=15,
                           textright='go')
stockage_usage.place(x=650, y=200)

threading.Thread(target=stockage_usage1).start()
threading.Thread(target=memory_usage1).start()
threading.Thread(target=cpu_usage1).start()
threading.Thread(target=network).start()

root.mainloop()
