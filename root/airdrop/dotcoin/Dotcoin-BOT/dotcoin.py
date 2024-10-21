import requests
import json
import os
from colorama import *
from datetime import datetime, timedelta
from dateutil import parser
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Dotcoin:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Profile': 'public',
            'Apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
            'Cache-Control': 'no-cache',
            'Host': 'api.dotcoin.bot',
            'Origin': 'https://app.dotcoin.bot',
            'Pragma': 'no-cache',
            'Referer': 'https://app.dotcoin.bot/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(f"{message}", flush=True)

    def welcome(self):
        print(
            f"""
        Auto Claim {Fore.BLUE + Style.BRIGHT}Dotcoin - BOT
            """
            f"""
        Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
    def get_token(self, query: str):
        url = 'https://api.dotcoin.bot/functions/v1/getToken'
        data = json.dumps({'initData': query})
        self.headers.update({
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if result:
            return result['token']
        else:
            return None
        
    def user_info(self, token: str):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_user_info'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def assets_info(self, token: str):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_assets'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def spinner(self, token: str):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/spin'
        data = json.dumps({})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def double_coins(self, token: str, coins: int):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/try_your_luck'
        data = json.dumps({'coins': coins})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def save_coins(self, token: str, taps: int):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/save_coins'
        data = json.dumps({'coins': taps})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def restore_attempts(self, token: str):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/restore_attempt'
        data = json.dumps({})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def upgrade_multitap(self, token: str, level: int):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/add_multitap'
        data = json.dumps({'lvl': level})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def upgrade_attempts(self, token: str, level: int):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/add_attempts'
        data = json.dumps({'lvl': level})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def upgrade_dtc_miner(self, token: str):
        url = 'https://api.dotcoin.bot/functions/v1/upgradeDTCMiner'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def tasks(self, token: str):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/get_filtered_tasks'
        data = json.dumps({"platform":"tdesktop","locale":"en","is_premium":False})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def complete_tasks(self, token: str, task_id: int):
        url = 'https://api.dotcoin.bot/rest/v1/rpc/complete_task'
        data = json.dumps({'oid': task_id})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()
    
    def question(self):
        while True:
            multitap_upgrade = 'n' #input("Upgrade Multitap Level? [y/n] -> ").strip().lower()
            if multitap_upgrade in ["y", "n"]:
                multitap_upgrade = multitap_upgrade == "y"
                break
            else:
                print(f"Invalid Input.Choose 'y' to upgrade or 'n' to skip.")
        multitap_count = 0
        if multitap_upgrade:
            while True:
                try:
                    multitap_count = int(input("How many times? -> "))
                    if multitap_count > 0:
                        break
                    else:
                        print(f"Please enter a positive number.")
                except ValueError:
                    print(f"Invalid input. Enter a number.")
        
        while True:
            attempts_upgrade = 'n' #input("Upgrade Limit Attempts? [y/n] -> ").strip().lower()
            if attempts_upgrade in ["y", "n"]:
                attempts_upgrade = attempts_upgrade == "y"
                break
            else:
                print(f"Invalid Input.Choose 'y' to upgrade or 'n' to skip.")
        attempts_count = 0
        if attempts_upgrade:
            while True:
                try:
                    attempts_count = int(input("How many times? -> "))
                    if attempts_count > 0:
                        break
                    else:
                        print(f"Please enter a positive number.")
                except ValueError:
                    print(f"Invalid input. Enter a number.")

        while True:
            miner_upgrade = 'y' #input("Upgarde DTC Mining Level? [y/n] -> ").strip().lower()
            if miner_upgrade in ["y", "n"]:
                miner_upgrade = miner_upgrade == "y"
                break
            else:
                print(f"Invalid Input.Choose 'y' to upgrade or 'n' to skip.")

        while True:
            go_spin = 'y' #input("Play Game Spinner? [y/n] -> ").strip().lower()
            if go_spin in ["y", "n"]:
                go_spin = go_spin == "y"
                break
            else:
                print(f"Invalid Input.Choose 'y' to play or 'n' to skip.")

        while True:
            go_task = 'y' #input("Check Available Tasks? [y/n] -> ").strip().lower()
            if go_task in ["y", "n"]:
                go_task = go_task == "y"
                break
            else:
                print(f"Invalid Input.Choose 'y' to check or 'n' to skip.")

        return multitap_upgrade, multitap_count, attempts_upgrade, attempts_count, miner_upgrade, go_spin, go_task
    
    def process_query(self, query: str, add_multitap: bool, multitap_count: int, add_attempts: bool, attempts_count: int, dtc_miner: bool, spinner: bool, check_task: bool):

        token = self.get_token(query)

        if token:
            user = self.user_info(token)
            if user:
                self.log(
                    f"[ Account {user['first_name']} ]"
                    f"[ Balance {user['balance']} Point ]"
                    f"[ Level {user['level']} ]"
                )
                time.sleep(1)

                self.log(f"[ Booster Info ]")
                time.sleep(1)
                self.log(
                    f"       -> Multitap Level   : "
                    f"{user['multiple_clicks']}"
                )
                self.log(
                    f"       -> Daily Attempts   : "
                    f"{user['limit_attempts']}"
                )
                self.log(
                    f"       -> DTC Mining Level : "
                    f"{user['dtc_level']}"
                )
                time.sleep(1)

                self.log(f"[ Assets Info ]")
                time.sleep(1)
                assets = self.assets_info(token)
                if assets:
                    for asset in assets:

                        if asset['symbol'] == 'VENOM':
                            self.log(
                                f"       -> Venom Amount     : "
                                f"{asset['amount']} ${asset['symbol']}"
                            )
                        else:
                            self.log(
                                f"       -> Dotcoin Amount   : "
                                f"{asset['amount']} ${asset['symbol']}"
                            )
                else:
                    self.log(f"[ Assets Info ] None")
                time.sleep(1)

                self.log(f"[ Upgrade Boost ]")
                time.sleep(1)
                if add_multitap:
                    for i in range(multitap_count):
                        user = self.user_info(token)
                        multitap_level = user['multiple_clicks']
                        upgrade = self.upgrade_multitap(token, multitap_level)
                        if upgrade['success']:
                            self.log(
                                f"       -> Multitap         : "
                                f"Upgrade Success"
                                f"- "
                                f"Level "
                                f"{multitap_level + 1}"
                            )
                        else:
                            self.log(
                                f"       -> Multitap         : "
                                f"Not Enough Balance"
                            )
                            break
                        time.sleep(1)
                else:
                    self.log(
                        f"       -> Multitap         : "
                        f"Skipped"
                    )
                time.sleep(1)

                self.log(f"[ Upgrade Boost ]")
                time.sleep(1)
                if add_attempts:
                    for i in range(attempts_count):
                        user = self.user_info(token)
                        attempts_level = user['limit_attempts'] - 9
                        upgrade = self.upgrade_attempts(token, attempts_level)
                        if upgrade['success']:
                            self.log(
                                f"       -> Limit Attempts   : "
                                f"Upgrade Success"
                                f"- "
                                f"Level "
                                f"{attempts_level + 1}"
                            )
                        else:
                            self.log(
                                f"       -> Limit Attempts   : "
                                f"Not Enough Balance"
                            )
                            break
                        time.sleep(1)
                else:
                    self.log(
                        f"       -> Limit Attempts   : "
                        f"Skipped"
                    )
                time.sleep(1)

                self.log(f"[ Upgrade Boost ]")
                time.sleep(1)
                if dtc_miner:
                    user = self.user_info(token)
                    miner_level = user['dtc_level']
                    upgrade = self.upgrade_dtc_miner(token)
                    if upgrade['success']:
                        self.log(
                            f"       -> DTC Mining       : "
                            f"Upgrade Success"
                            f"- "
                            f"Level "
                            f"{miner_level + 1}"
                        )
                    else:
                        self.log(
                            f"       -> DTC Mining       : "
                            f"Upgrade Failed"
                        )
                else:
                    self.log(
                        f"       -> DTC Mining       : "
                        f"Skipped"
                    )
                time.sleep(1)

                if spinner:
                    self.log(
                        f"[ Play Game ] "
                        f"Spinner"
                    )
                    time.sleep(1)

                    assets = self.assets_info(token)
                    for asset in assets:
                        if asset['symbol'] == 'DTC':
                            dtc_amount = asset['amount']

                            if dtc_amount >= 5:

                                spinner_time = parser.isoparse(user['spin_updated_at'])
                                spinner_time_wib = spinner_time.astimezone(wib)
                                spinner_ready = (spinner_time_wib + timedelta(hours=8)).strftime('%x %X %Z')

                                spin = self.spinner(token)
                                if spin['success']:
                                    if spin['symbol'] == 'VENOM':
                                        self.log(
                                            f"       -> Spinner : "
                                            f"Success"
                                            f"- "
                                            f"Reward "
                                            f"{spin['amount']} $VENOM"
                                        )
                                    else:
                                        self.log(
                                            f"       -> Spinner : "
                                            f"Success"
                                            f"- "
                                            f"Reward "
                                            f"{spin['amount']} $DTC"
                                        )
                                else:
                                    self.log(
                                        f"       -> Spinner : "
                                        f"Already Play Spinner"
                                    )
                                    self.log(
                                        f"       -> Spinner : "
                                        f"Comeback at "
                                        f"{spinner_ready}"
                                    )
                                time.sleep(1)
                            else:
                                self.log(
                                    f"       -> Spinner : "
                                    f"Not Enough DTC"
                                )
                                self.log(
                                    f"       -> Amount  : "
                                    f"{dtc_amount} $DTC"
                                )
                else:
                    self.log(
                        f"[ Play Game ] "
                        f"Spinner Skipped"
                    )
                time.sleep(1)

                self.log(
                    f"[ Play Game ] "
                    f"Double Coins"
                )
                time.sleep(1)
                if user['gamex2_times'] != 0:
                    coins = 150000
                    gacha = self.double_coins(token, coins)
                    if gacha['success']:
                        self.log(
                            f"       -> Gacha   : "
                            f"WIN"
                            f"- "
                            f"Reward "
                            f"{coins}"
                        )
                    else:
                        self.log(
                            f"       -> Gacha   : "
                            f"LOSE"
                        )
                else:
                    self.log(
                        f"       -> Gacha   : "
                        f"Already Gacha Today"
                    )
                time.sleep(1)

                self.log(
                    f"[ Play Game ] "
                    f"Tap Tap"
                )
                time.sleep(1)
                energy = user['daily_attempts']
                self.log(
                    f"       -> Tap Tap : "
                    f"Energy {energy}"
                )
                time.sleep(1)
                while energy > 0:
                    for _ in range(energy):
                        time.sleep(3)
                        taps = self.save_coins(token, 20000)
                        if taps['success']:
                            self.log(
                                f"       -> Tap Tap : "
                                f"Success"
                            )
                        else:
                            self.log(
                                f"       -> Tap Tap : "
                                f"Failed"
                            )
                    user = self.user_info(token)
                    energy = user['daily_attempts']
                    if energy == 0:
                        count = 0
                        while count < 1:
                            restore = self.restore_attempts(token)
                            if restore['success'] and restore:
                                self.log(
                                    f"       -> Tap Tap : "
                                    f"Restore Energy Success"
                                )
                            else:
                                self.log(
                                    f"       -> Tap Tap : "
                                    f"Restore Energy Reached Limit"
                                )
                                count += 1
                            time.sleep(1)
                            user = self.user_info(token)
                            energy = user['daily_attempts']
                else:
                    self.log(
                        f"       -> Tap Tap : "
                        f"Energy has Run Out"
                    )
                time.sleep(1)

                if check_task:
                    self.log(
                        f"[ Check Task ] "
                        f"Checked"
                    )
                    tasks = self.tasks(token)
                    if tasks:
                        for task in tasks:
                            task_id = task['id']

                            if task['is_completed'] is None:

                                complete = self.complete_tasks(token, task_id)
                                if complete['success']:
                                    self.log(
                                        f"       -> Task"
                                        f"{task['title']} "
                                        f"Completed"
                                        f"- "
                                        f"Reward "
                                        f"{task['reward']}"
                                    )
                                else:
                                    self.log(
                                        f"       -> Task"
                                        f"{task['title']} "
                                        f"Not Completed"
                                    )
                                time.sleep(1)
                    else:
                        self.log(
                            f"       -> Task"
                            f"Failed to Checked Tasks"
                        )
                    time.sleep(1)
                else:
                    self.log(
                        f"[ Check Task ] "
                        f"Skipped"
                    )
                time.sleep(1)

            else:
                self.log(f"[ Account None ]")
                time.sleep(1)

        else:
            self.log(f"[ Token None ]")
            time.sleep(1)
        
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            add_multitap, multitap_count, add_attempts, attempts_count, dtc_miner, spinner, check_task = self.question()

            while True:
                self.log(
                    f"Account's Total: "
                    f"{len(queries)}"
                )

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, add_multitap, multitap_count, add_attempts, attempts_count, dtc_miner, spinner, check_task)
                        self.log(f"-" * 75)
                print("KELUAR")
                break
                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"[ Wait for"
                        f"{formatted_time} "
                        f"... ]",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Dotcoin - BOT")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}")

if __name__ == "__main__":
    dotcoin = Dotcoin()
    dotcoin.main()