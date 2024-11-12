### Nodepay Automate with Proxies Bypass Version

![nodepay](assets/image.png)

### Tools and components required

1. Nodepay Account| Register: [https://app.nodepay.ai/register](https://app.nodepay.ai/register?ref=fkCYv2psxv9YkrM)
2. Proxies Static Residental
3. VPS (OPTIONAL) and Python3

# Setup Tutorial

- Open [Nodepay](https://app.nodepay.ai/register?ref=ZUCBuJaIoBXLE6J) and login to dashboard
- Press F12 or CTRL + SHIFT + I
- Select Console
- At the console, type ```allow pasting``` and press enter
- Then type ``localStorage.getItem('np_token')`` and press enter
- The text that appears is your nodepay token and copy the text

### Component installation

- Install Python For Windows: [Python](https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe)
- For Unix:
```bash
apt install python3 python3-pip -y
```
- Clone project repository
```bash
git clone https://github.com/Rambeboy/nodepay.git && cd nodepay
```
- Install requirements: 
```bash
python -m pip install -r requirements.txt
```

### Run the Bot

Replace the proxies example in ```proxies.txt``` to your own proxies, please use only 10 proxies with proxies http only.

#### Run command

- Run for original server:
```bash
python run.py
```
- Run for bypass server:
>Use this script if you getting errors like ```Error during API call: 403 Client Error: Forbidden for url``` 

```bash
python run-bypass.py
```
- Press Enter then insert your nodepay token

# Operating status

If the following log appears, it means it is running successfully.
```bash
2024-07-30 04:37:18.263 | INFO     | __main__:ping:110 - Ping successful: {'success': True, 'code': 0, 'msg': 'Success', 'data': {'ip_score': 88}}
2024-07-30 04:37:48.621 | INFO     | __main__:ping:110 - Ping successful: {'success': True, 'code': 0, 'msg': 'Success', 'data': {'ip_score': 90}}
2024-07-30 04:38:18.968 | INFO     | __main__:ping:110 - Ping successful: {'success': True, 'code': 0, 'msg': 'Success', 'data': {'ip_score': 94}}
2024-07-30 04:38:59.338 | INFO     | __main__:ping:110 - Ping successful: {'success': True, 'code': 0, 'msg': 'Success', 'data': {'ip_score': 98}}
```
# Notes

- Run this bot, and it will update your referrer code to my invite code if you don't have one.
- One account only can connect with 10 Proxies
- You can just run this bot at your own risk, I'm not responsible for any loss or damage caused by this bot. This bot is for educational purposes only.
