add-auto-load-safe-path vmlinux-gdb.py
set substitute-path /home/wroathe .

source vmtools.py

target remote :1234
