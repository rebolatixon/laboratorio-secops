import psutil
import datetime


print("=" * 50)
print(f"Monitorização do Sistema - {datetime.datetime.now()}")
print("=" * 50)


# CPU
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU: {cpu_percent}% usado")


# Memória RAM
mem = psutil.virtual_memory()
print(f"RAM: {mem.percent}% usado (Total: {mem.total // (1024**3)} GB)")


# Disco
disk = psutil.disk_usage('/')
print(f"Disco (/): {disk.percent}% usado (Livre: {disk.free // (1024**3)} GB)")



