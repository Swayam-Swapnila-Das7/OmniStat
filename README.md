```markdown
# OmniStat

A lightweight CLI tool to monitor system resources (CPU, RAM, Storage, Temperature, and Battery) using Python and `psutil`.

## Features

* **CPU Status:** Monitor core count and excessive load.
* **Disk Status:** Check total, used, and free storage space.
* **RAM Status:** Track memory usage and availability.
* **Hardware Temperature:** Monitor CPU, NVMe SSD, and GPU temperatures.
* **Battery Status:** View charge percentage, remaining time, and power state.

## Hardware & OS Compatibility

OmniStat was created and tested on **Void Linux** using an **AMD CPU**, **NVMe SSD**, and **AMD GPU**. 

*Some hardware temperature sensors (like `k10temp`, `acpitz`, `nvme`, or `amdgpu`) depend heavily on specific kernel modules and hardware vendors. If you run this script on other operating systems (like Windows or macOS) or non-AMD hardware, certain temperature functions may show errors or return no output.*

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Swayam-Swapnila-Das7/OmniStat.git](https://github.com/Swayam-Swapnila-Das7/OmniStat.git)
   cd OmniStat

```

2. **Create and activate a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



## Usage

Run the script from your terminal with one or more options:

```bash
python OmniStat.py [options]

```

### Options

* `-c` : Check CPU status and usage
* `-d` : Check SSD/HDD storage status
* `-r` : Check RAM usage and availability
* `-t` : Monitor hardware temperatures
* `-b` : Check battery percentage and time left

*Note: You can use more than one function at a time just by adding a space between them (e.g., `python script.py -c -r`).*

## Author

* **Swayam Swapnila Das**
* GitHub: [Swayam-Swapnila-Das7](https://github.com/Swayam-Swapnila-Das7)
* LinkedIn: [swayam-swapnila-das](https://www.google.com/search?q=https://linkedin.com/in/swayam-swapnila-das)

```

```
