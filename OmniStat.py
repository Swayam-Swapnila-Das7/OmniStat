try :
	import psutil
	import sys
except ModuleNotFoundError :
	print('[WARRNING] Module not found')
	exit()
except Exception as e :
	print(f'[WARRNING] : {e}')
	exit()

GiB = 1024 ** 3
MiB = 1024 ** 2

class color :
	RED    = "\033[1;31m"
	GREEN  = "\033[1;32m"
	YELLOW = "\033[33m"
	BLUE  = "\033[34m"
	DARKCYAN = '\033[36m'
	PURPLE = "\033[1;35m"
	RESET  = "\033[0m"

def check_disk_status() :

	disk = psutil.disk_usage('/')
	total_space = disk.total / GiB
	used_space = disk.used / GiB
	free_space = disk.free / GiB

	print(color.PURPLE+'\n\n=========== SSD/HDD STORAGE STATUS ===========\n'+color.RESET)
	print(color.YELLOW+f' Total Space : {total_space:.2f} GiB'+color.RESET)
	print(color.YELLOW+f' Used Space : {used_space:.2f} GiB'+color.RESET)
	print(color.YELLOW+f' Free Space : {free_space:.2f} GiB'+color.RESET)

	if disk.percent > 85 :
		print(color.RED+f' [WARRNING] You are running out of storage soon !\n  Now your disk is {disk.percent:.2f}% in used !'+color.RESET)
	else :
		print(color.GREEN+f' [SAFE] You have good enough storage .\n  Your disk is {disk.percent:.2f} % used .'+color.RESET)

def check_cpu_status():

	cpu_cores = psutil.cpu_count(logical = False)
	cpu_usage = psutil.cpu_percent(interval = 1)
	print(color.PURPLE+'\n\n=========== CPU STATUS ===========\n'+color.RESET)
	print(color.YELLOW+f'[+]Your CPU have {cpu_cores} cores.'+color.RESET)
	if cpu_usage > 85 :
		print(color.RED+f'[WARRNING] Your CPU is on excesive load.\n Running at {cpu_usage:.2f} %'+color.RESET)
	else :
		print(color.GREEN+f'[SAFE] Your CPU is working in safe limit. \n Running at {cpu_usage:.2f} %'+color.RESET)

def check_ram_status():
	ram = psutil.virtual_memory()
	total_ram = ram.total/GiB
	used_ram = ram.used/GiB
	available_ram = ram.available/GiB

	print(color.PURPLE+'\n\n=========== RAM STATUS ===========\n'+color.RESET)
	print(color.YELLOW+f' Total RAM : {total_ram:.2f} GiB'+color.RESET)
	print(color.YELLOW+f' Used RAM : {used_ram:.2f} GiB'+color.RESET)
	print(color.YELLOW+f' Available RAM : {available_ram:.2f} GiB'+color.RESET)

	if ram.percent > 85 :
		print(color.RED+f' [WARRNING] Your RAM is running out soon !\n  Now your RAM is {ram.percent:.2f}% in used !'+color.RESET)
	else :
		print(color.GREEN+f' [SAFE] You have good enough RAM .\n  Your RAM is {ram.percent:.2f}% used .'+color.RESET)

def check_temperature() :
	temperature = psutil.sensors_temperatures(fahrenheit=False)
	print(color.PURPLE+'\n\n=========== HARDWARE TEMPERATURE MONITOR ==========='+color.RESET)
	if 'k10temp' in temperature :
		print(color.BLUE+'\n[+] CPU CORE TEMPERATURE : '+color.RESET)
		print(color.DARKCYAN+'      Label   Temperature'+color.RESET)
		print(color.DARKCYAN+'      -----   -----------'+color.RESET)
		for sensor in temperature['k10temp'] :
			label = sensor.label if sensor.label else "Core"
			print(color.YELLOW+f'      {label}   {sensor.current:.2f} °C'+color.RESET)
	
	if 'acpitz' in temperature :
		print(color.BLUE+'\n[+] MOTHERBOARD(CPU Socket) TEMPERATURE : '+color.RESET)
		print(color.DARKCYAN+'      Label   Temperature'+color.RESET)
		print(color.DARKCYAN+'      -----   -----------'+color.RESET)
		for sensor in temperature['acpitz'] :
			label = sensor.label if sensor.label else "BOARD"
			print(color.YELLOW+f'      {label}   {sensor.current:.2f} °C'+color.RESET)

	if 'nvme' in temperature :
		print(color.BLUE+'\n[+] NVMe SSD TEMPERATURE : '+color.RESET)
		print(color.DARKCYAN+'      Label   Temperature'+color.RESET)
		print(color.DARKCYAN+'      -----   -----------'+color.RESET)
		for sensor in temperature['nvme'] :
			label = sensor.label if sensor.label else "SSD"
			print(color.YELLOW+f'      {label}   {sensor.current:.2f} °C'+color.RESET)

	if 'amdgpu' in temperature :
		print(color.BLUE+'\n[+]GPU CORE TEMPERATURE : '+color.RESET)
		print(color.DARKCYAN+'      Label   Temperature'+color.RESET)
		print(color.DARKCYAN+'      -----   -----------'+color.RESET)
		for sensor in temperature['amdgpu'] :
			label = sensor.label if sensor.label else "GPU"
			print(color.YELLOW+f'      {label}   {sensor.current:.2f} °C'+color.RESET)

def check_battery() :
	battery = psutil.sensors_battery()
	if battery.power_plugged :
		plug_status = 'CHARGING'
		hh,mm,ss = 00,00,00
	else :
		plug_status = 'DISCHARGING'
		time_remain = battery.secsleft
		hh = time_remain//(60*60)
		time_remain = time_remain%(60*60)
		mm = time_remain//60
		time_remain = time_remain%60
		ss = time_remain
		

	print(color.PURPLE+'\n\n=========== BATTERY STATUS CHECK ==========='+color.RESET)
	print(color.YELLOW+f'  CHARGE : {battery.percent:.2f} %\n  TIME LEFT : {hh}:{mm}:{ss}\n  POWER PLUGGED STATUS : {plug_status}'+color.RESET)

def show_help() :
	help_text = '''
	------------------------------------------------------
	|                     OmniStat                       |
	|----------------------------------------------------|
	| Usage: python script.py [options]                  |
	|                                                    |
	| Options:                                           |
	|   -c    Check CPU status and usage                 |
	|   -d    Check SSD/HDD storage status               |
	|   -r    Check RAM usage and availability           |
	|   -t    Monitor hardware temperatures              |
	|   -b    Check battery percentage and time left     |
	|                                                    |
	| NOTE : You can use more than one function at       |
	|        a time just use space between them          |
	|                                                    |
	| Author: Swayam Swapnila Das                        |
	| GitHub: https://github.com/Swayam-Swapnila-Das7    |
	| LinkedIn: in/swayam-swapnila-das                   |
	------------------------------------------------------
		'''
	for line in help_text.splitlines() :
		print(f"\033[1;37;44m{line}\033[0m")

system_tools = {'-c' : check_cpu_status ,
				'-d' : check_disk_status ,
				'-r' : check_ram_status ,
				'-t' : check_temperature,
				'-b' : check_battery,
				}

def check_args(arguments):
	for arg in arguments :
		if ( not arg.strip() in system_tools) :
			print('Invalid Argument Passed !')
			break

def main():
	arguments = sys.argv[1:]
	if len(arguments) >= 1 :
		check_args(arguments)
	else :
		show_help()
	for arg in arguments :
		action = system_tools.get(arg.strip())
		try :
			action()
		except Exception as e :
			print(color.BLUE +f' Apologies, it appears this function is not operating correctly due to potential restriction or limitations. !'+color.RESET)

if __name__ == '__main__':
	main()
