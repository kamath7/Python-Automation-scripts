import psutil

print(psutil.cpu_count(logical=False))
print(psutil.cpu_percent(interval=5))
print(psutil.cpu_times())
print(psutil.cpu_stats())