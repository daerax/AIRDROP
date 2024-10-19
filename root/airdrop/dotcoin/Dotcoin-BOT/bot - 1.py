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
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Dotcoin - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
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
            miner_upgrade = input("Upgarde DTC Mining? [y/n] -> ").strip().lower()
            if miner_upgrade in ["y", "n"]:
                miner_upgrade = miner_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")

        while True:
            go_spin = input("Play Game Spinner? [y/n] -> ").strip().lower()
            if go_spin in ["y", "n"]:
                go_spin = go_spin == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to play or 'n' to skip.{Style.RESET_ALL}")

        while True:
            go_task = input("Check Available Tasks? [y/n] -> ").strip().lower()
            if go_task in ["y", "n"]:
                go_task = go_task == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to check or 'n' to skip.{Style.RESET_ALL}")

        return miner_upgrade, go_spin, go_task
    
    def process_query(self, query: str, dtc_miner: bool, spinner: bool, check_task: bool):

        token = self.get_token(query)

        if token:
            user = self.user_info(token)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['first_name']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['balance']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}Point ] [ Level{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['level']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Booster Info ]{Style.RESET_ALL}")
                time.sleep(1)
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Multitap Level   : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{user['multiple_clicks']}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Daily Attempts   : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{user['limit_attempts']}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining Level : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}{user['dtc_level']}{Style.RESET_ALL}"
                )
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Assets Info ]{Style.RESET_ALL}")
                time.sleep(1)
                assets = self.assets_info(token)
                if assets:
                    for asset in assets:

                        if asset['symbol'] == 'VENOM':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Venom Amount     : {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{asset['amount']} ${asset['symbol']}{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Dotcoin Amount   : {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{asset['amount']} ${asset['symbol']}{Style.RESET_ALL}"
                            )
                else:
                    self.log(f"{Fore.RED+Style.BRIGHT}[ Assets Info ] None{Style.RESET_ALL}")
                time.sleep(1)

                self.log(f"{Fore.CYAN+Style.BRIGHT}[ Upgrade Boost ]{Style.RESET_ALL}")
                time.sleep(1)
                if dtc_miner:
                    upgrade = self.upgrade_dtc_miner(token)
                    if upgrade['success']:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}Upgrade Success{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}Level {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}{user['dtc_level'] + 1}{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}Upgrade Failed{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> DTC Mining       : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if spinner:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT}Spinner{Style.RESET_ALL}"
                    )
                    time.sleep(1)

                    spinner_time = parser.isoparse(user['spin_updated_at'])
                    spinner_time_wib = spinner_time.astimezone(wib)
                    spinner_ready = (spinner_time_wib + timedelta(hours=8)).strftime('%x %X %Z')

                    spin = self.spinner(token)
                    if spin['success']:
                        if spin['symbol'] == 'VENOM':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{spin['amount']} $VENOM{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT}{spin['amount']} $DTC{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}Already Play Spinner{Style.RESET_ALL}"
                        )
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Spinner : {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}Comeback at {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}{spinner_ready}{Style.RESET_ALL}"
                        )
                    time.sleep(1)
                else:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Spinner Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(
                    f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Double Coins{Style.RESET_ALL}"
                )
                time.sleep(1)
                if user['gamex2_times'] != 0:
                    coins = 150000
                    gacha = self.double_coins(token, coins)
                    if gacha['success']:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}WIN{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT}{coins}{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}LOSE{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Gacha   : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Already Gacha Today{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.log(
                    f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Tap Tap{Style.RESET_ALL}"
                )
                time.sleep(1)
                energy = user['daily_attempts']
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT}Energy {energy}{Style.RESET_ALL}"
                )
                time.sleep(1)
                while energy > 0:
                    for _ in range(energy):
                        time.sleep(3)
                        taps = self.save_coins(token, 20000)
                        if taps['success']:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Failed{Style.RESET_ALL}"
                            )
                    user = self.user_info(token)
                    energy = user['daily_attempts']
                    if energy == 0:
                        count = 0
                        while count < 1:
                            restore = self.restore_attempts(token)
                            if restore['success'] and restore:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Restore Energy Success{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Restore Energy Reached Limit{Style.RESET_ALL}"
                                )
                                count += 1
                            time.sleep(1)
                            user = self.user_info(token)
                            energy = user['daily_attempts']
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Tap Tap : {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Energy has Run Out{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if check_task:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Check Task ] {Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT}Checked{Style.RESET_ALL}"
                    )
                    tasks = self.tasks(token)
                    if tasks:
                        for task in tasks:
                            task_id = task['id']

                            if task['is_completed'] is None:

                                complete = self.complete_tasks(token, task_id)
                                if complete['success']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Completed{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} - {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}Reward {Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT}{task['reward']}{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Not Completed{Style.RESET_ALL}"
                                    )
                                time.sleep(1)
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}       -> Task{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}Failed to Checked Tasks{Style.RESET_ALL}"
                        )
                    time.sleep(1)
                else:
                    self.log(
                        f"{Fore.CYAN+Style.BRIGHT}[ Check Task ] {Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    )
                time.sleep(1)

            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Account None ]{Style.RESET_ALL}")
                time.sleep(1)

        else:
            self.log(f"{Fore.RED+Style.BRIGHT}[ Token None ]{Style.RESET_ALL}")
            time.sleep(1)
        
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            dtc_miner, spinner, check_task = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, dtc_miner, spinner, check_task)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Dotcoin - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    dotcoin = Dotcoin()
    dotcoin.main()