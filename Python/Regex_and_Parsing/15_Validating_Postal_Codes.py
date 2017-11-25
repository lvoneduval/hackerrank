import re
regs = [r'^[1-9]([0-9]){5}$']
noreg = [r'([\d]).\1*([\d]).\2',r'([\d])([\d])\1\2']
s = input()
print(all(bool(re.search(r,s)) for r in regs) and not any(re.search(r,s) for r in noreg))
