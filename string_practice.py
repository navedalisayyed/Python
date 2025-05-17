import os
terminal_width=os.get_terminal_size().columns
str=input("Enter your string ")
print(str.center(terminal_width).title())
print(str.ljust(terminal_width).title())
print(str.rjust(terminal_width).title())
