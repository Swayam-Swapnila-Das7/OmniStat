#! /usr/bin/env python3

try :
	import sys
	from core.scan import system_scanning,color
except ModuleNotFoundError :
	print('[WARNING] Module not found')
	exit()
except Exception as e :
	print(f'[WARNING] : {e}')
	exit()

system_scanning = system_scanning()
color = color()

def check_args(arguments):
	for arg in arguments :
		if ( not arg.strip() in system_tools) :
			print(color.RED+f"Invalid Argument Passed!"+color.RESET)
			exit()

system_tools = {'-c' : system_scanning.check_cpu_status ,
                '-d' : system_scanning.check_disk_status ,
                '-r' : system_scanning.check_ram_status ,
                '-t' : system_scanning.check_temperature,
                '-b' : system_scanning.check_battery,
                }

def main():
	arguments = sys.argv[1:]
	if len(arguments) >= 1 :
		check_args(arguments)
	else :
		system_scanning.show_help()
	for arg in arguments :
		action = system_tools.get(arg.strip())
		try :
			action()
		except Exception as e :
			print(color.BLUE +f' Apologies, it appears this function is not operating correctly due to potential restriction or limitations. !'+color.RESET)

if __name__ == '__main__':
	main()
