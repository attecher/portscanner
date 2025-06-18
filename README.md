## 🔍 Portscanner
a practice tool
This is a lightweight Python script that scans one or multiple IP addresses for open ports. It's useful for basic network diagnostics or educational purposes.

## 🛠 Features

- Scan a **single** or **multiple IP addresses**
- Specify how many ports to scan (from port 1 up to your input)
- Color-coded output for open ports (using `termcolor`)

---

## 💻 Requirements

- Python 3.x
- `termcolor` module

Install `termcolor` if not already installed:

```bash
pip install termcolor
````

---

## ▶️ Usage

```bash
python port_scanner.py
```

Then follow the prompts:

```
[*] Enter the ipaddress( put , in between for multiple ip's): 192.168.1.1,192.168.1.2
[*] Enter the number of ports : 100
```

---

## 📦 Example Output

```
[*] Scanning Multiple Targets

Scanning Start For 192.168.1.1
[+] Port opened 22
[+] Port opened 80

Scanning Start For 192.168.1.2
[+] Port opened 21
```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing** only. Scanning systems without permission may violate laws and is strictly prohibited.

---

