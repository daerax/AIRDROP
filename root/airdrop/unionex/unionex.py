from colorama import *
from datetime import datetime, timedelta
from fake_useragent import FakeUserAgent
from faker import Faker
from requests import (
    JSONDecodeError,
    RequestException,
    Session
)
from time import sleep
import json
import os
import sys

class UnionEx:
    def __init__(self) -> None:
        self.session = Session()
        self.faker = Faker()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Host': 'activity.unionex.com',
            'Origin': 'https://activity.unionex.com',
            'Pragma': 'no-cache',
            'Priority': 'u=3, i',
            'Referer': 'https://activity.unionex.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': FakeUserAgent().random
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_timestamp(self, message):
        print(
            f"{message}",
            flush=True
        )

    def login_user(self, queries: str):
        url = 'https://activity.unionex.com/api/uxp/user/login'
        accounts = []
        for query in queries:
            try:
                data = json.dumps({'tgData':query,'inviteCode':'YfN9MSZM'})
                headers = {
                    **self.headers,
                    'Content-Length': str(len(data)),
                    'Content-Type': 'application/json; charset=utf-8'
                }
                response = self.session.post(url=url, headers=headers, data=data)
                response.raise_for_status()
                token = response.json()['data']['token']
                accounts.append({'query': query, 'token': token})
            except (Exception, JSONDecodeError, RequestException) as e:
                self.print_timestamp(
                    f"{Fore.YELLOW + Style.BRIGHT}[ Failed To Process {query} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}[ {str(e)} ]{Style.RESET_ALL}"
                )
                continue
        return accounts

    def check_in_user(self, token: str, query: str):
        url = 'https://activity.unionex.com/api/uxp/user/checkIn'
        try:
            data = json.dumps({'tgData':query})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ An HTTP Error Occurred While CheckIn: {str(e.response.reason)} ]{Style.RESET_ALL}")
            return None
        except (Exception, JSONDecodeError) as e:
            self.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ An Unexpected Error Occurred While CheckIn: {str(e)} ]{Style.RESET_ALL}")
            return None

    def enter_user(self, token: str):
        url = 'https://activity.unionex.com/api/uxp/user/enter'
        try:
            data = json.dumps({})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return True
        except (Exception, JSONDecodeError, RequestException):
            return False

    def detail_user(self, token: str):
        url = 'https://activity.unionex.com/api/uxp/user/detail'
        try:
            data = json.dumps({})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ An HTTP Error Occurred While CheckIn: {str(e.response.reason)} ]{Style.RESET_ALL}")
            return None
        except (Exception, JSONDecodeError) as e:
            self.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ An Unexpected Error Occurred While CheckIn: {str(e)} ]{Style.RESET_ALL}")
            return None

    def user_claim_tg(self, token: str):
        url = 'https://activity.unionex.com/api/uxp/user/claimTg'
        try:
            data = json.dumps({})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return True
        except (Exception, JSONDecodeError, RequestException):
            return False

    def user_claim_x(self, token: str):
        url = 'https://activity.unionex.com/api/uxp/user/claimX'
        try:
            data = json.dumps({})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return True
        except (Exception, JSONDecodeError, RequestException):
            return False

    def user_claim_share(self, token: str):
        url = 'https://activity.unionex.com/api/uxp/user/claimShare'
        try:
            data = json.dumps({})
            headers = {
                **self.headers,
                'Authorization': token,
                'Content-Length': str(len(data)),
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            return True
        except (Exception, JSONDecodeError, RequestException):
            return False

    def main(self):
        while True:
            try:
                queries = [line.strip() for line in open('queries.txt') if line.strip()]
                accounts = self.login_user(queries=queries)
                total_bonus = 0

                self.print_timestamp(f"{Fore.WHITE + Style.BRIGHT}[ Home ]{Style.RESET_ALL}")
                for account in accounts:
                    check_in_user = self.check_in_user(token=account['token'], query=account['query'])
                    if check_in_user is None: continue

                    self.enter_user(token=account['token'])
                    detail_user = self.detail_user(token=account['token'])
                    if detail_user is None: continue
                    self.print_timestamp(
                        f"{Fore.CYAN + Style.BRIGHT}[ {detail_user['data']['nickname']} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.CYAN + Style.BRIGHT}[ Balance {detail_user['data']['totalBonus']} ]{Style.RESET_ALL}"
                    )

                    if check_in_user['data']['result']:
                        self.print_timestamp(
                            f"{Fore.CYAN + Style.BRIGHT}[ {detail_user['data']['nickname']} ]{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT}[ You Have Got {detail_user['data']['checkInBonus']} From Daily Check In ]{Style.RESET_ALL}"
                        )
                    else:
                        self.print_timestamp(
                            f"{Fore.CYAN + Style.BRIGHT}[ {detail_user['data']['nickname']} ]{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Already Claim Daily Check In ]{Style.RESET_ALL}"
                        )
                    
                    self.user_claim_tg(token=account['token'])
                    self.user_claim_x(token=account['token'])
                    self.user_claim_share(token=account['token'])

                    total_bonus += detail_user['data']['totalBonus']

                self.print_timestamp(
                    f"{Fore.CYAN + Style.BRIGHT}[ Total Account {len(accounts)} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.GREEN + Style.BRIGHT}[ Total Bonus {total_bonus} ]{Style.RESET_ALL}"
                )

                sleep_timestamp = (datetime.now().astimezone() + timedelta(seconds=3600)).strftime('%x %X %Z')
                self.print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Restarting At {sleep_timestamp} ]{Style.RESET_ALL}")
                print("KELUAR")
                break
                sleep(3600)
                self.clear_terminal()
            except Exception as e:
                self.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ {str(e)} ]{Style.RESET_ALL}")
                continue

if __name__ == '__main__':
    try:
        init(autoreset=True)
        unionex = UnionEx()
        unionex.main()
    except (ValueError, IndexError, FileNotFoundError) as e:
        unionex.print_timestamp(f"{Fore.RED + Style.BRIGHT}[ {str(e)} ]{Style.RESET_ALL}")
    except KeyboardInterrupt:
        sys.exit(0)