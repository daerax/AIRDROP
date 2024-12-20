import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime
import secrets
from urllib.parse import parse_qs, unquote
def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File query.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

def print_(word):
    print(f"{word}")

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://www.yescoin.gold',
    'Referer': 'https://www.yescoin.gold/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def parse_and_reconstruct(url_encoded_string):
    parsed_data = urllib.parse.parse_qs(url_encoded_string)
    user_data_encoded = parsed_data.get('user', [None])[0]
    
    if user_data_encoded:
        user_data_json = urllib.parse.unquote(user_data_encoded)
    else:
        user_data_json = None
    
    reconstructed_string = f"user={user_data_json}"
    for key, value in parsed_data.items():
        if key != 'user':
            reconstructed_string += f"&{key}={value[0]}"
    
    return reconstructed_string

def generate_random_hex(length=32):
    return secrets.token_hex(length // 2)

def login(query, useragent):
    url = 'https://bi.yescoin.gold/user/login'
    headers['User-Agent'] = useragent
    payload = {
        'code': f'{query}'
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getgameinfo(token, useragent):
    url = 'https://bi.yescoin.gold/game/getGameInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getaccountinfo(token, useragent):
    url = 'https://bi.yescoin.gold/account/getAccountInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialboxreloadpage(token, useragent):
    url = 'https://bi.yescoin.gold/game/specialBoxReloadPage'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialboxinfo(token, useragent):
    url = 'https://bi.yescoin.gold/game/getSpecialBoxInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getacccountbuildinfo(token, useragent):
    url = 'https://bi.yescoin.gold/build/getAccountBuildInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None


def collectCoin(token, useragent, count):
    url = 'https://bi.yescoin.gold/game/collectCoin'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=count)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialbox(token, useragent):
    url = 'https://bi.yescoin.gold/game/recoverSpecialBox'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getcoinpool(token, useragent):
    url = 'https://bi.yescoin.gold/game/recoverCoinPool'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def collectspecialbox(token, useragent, payload):
    url = 'https://bi.yescoin.gold/game/collectSpecialBoxCoin'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getwallet(token, useragent):
    url = 'https://bi.yescoin.gold/wallet/getWallet'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def offline(token, useragent):
    url = 'https://bi.yescoin.gold/user/offline'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_daily(token, useragent):
    url = 'https://bi.yescoin.gold/mission/getDailyMission'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def finish_daily(token, useragent, mission_id):
    url = 'https://bi.yescoin.gold/mission/finishDailyMission'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=mission_id)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_finish_status_task(token, useragent):
    url = 'https://bi.yescoin.gold/task/getFinishTaskBonusInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_account_build_info(token, useragent):
    url = 'https://bi.yescoin.gold/build/getAccountBuildInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_task_list(token, useragent):
    url = 'https://bi.yescoin.gold/task/getTaskList'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def check_task_status(token, useragent, task_id):
    url = 'https://bi.yescoin.gold/task/checkTask'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=task_id)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None
    
def claim_reward_task(token, useragent, task_id):
    url = 'https://bi.yescoin.gold/task/claimTaskReward'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=task_id)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None
    
def claim_bonus_task(token, useragent, id):
    url = 'https://bi.yescoin.gold/task/claimBonus'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=id)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def level_up(token, useragent, id):
    url = 'https://bi.yescoin.gold/build/levelUp'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=id)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None
    
def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")

def parse_query(query: str):
    parsed_query = parse_qs(query)
    parsed_query = {k: v[0] for k, v in parsed_query.items()}
    user_data = json.loads(unquote(parsed_query['user']))
    parsed_query['user'] = user_data
    return parsed_query

def main():
    queries = load_credentials()
    tokens = [None] * len(queries)
    walletaddr = [None] * len(queries)
    giftboxs = [0] * len(queries)

    selector_upgrade = 'n' #input("Auto Upgrade level y/n  : ").strip().lower()
    interval_giftbox = 3600
    while True:
        for index, query in enumerate(queries):
            parse = parse_query(query)
            user = parse.get('user')
            currentTime = int(time.time())
            useragent = getuseragent(index)
            user_data = parse_and_reconstruct(query)
            token = tokens[index]
            if token is None:
                datalogin = login(user_data, useragent)
                if datalogin is not None:
                    codelogin = datalogin.get('code')
                    if codelogin == 0:
                        data = datalogin.get('data')
                        tokendata = data.get('token')
                        tokens[index] = tokendata
                        print_("Refresh Token")
                    else:
                        print_(f"{datalogin.get('message')}")

            token = tokens[index]
            #GET ACCOUNT INFO
            data_account_info = getaccountinfo(token, useragent)
            if data_account_info is not None:
                code = data_account_info.get('code')
                if code == 0:
                    username = user.get('username')
                    data = data_account_info.get('data')
                    currentAmount = data.get('currentAmount')
                    levelInfo = data.get('levelInfo')
                    rankName = levelInfo.get('rankName')
                    level = levelInfo.get('level')
                    print_(f"-- Username : {username} | Level : {rankName} - {level} | Balance : {currentAmount}")

            #Daily Mission
            daily = get_daily(token, useragent)
            if daily is not None:
                print_('Get Daily Mission')
                data = daily.get('data')
                for da in data:
                    missionStatus = da.get('missionStatus')
                    name = da.get('name')
                    missionId = da.get('missionId')
                    if missionStatus == 0:
                        time.sleep(2)
                        finish_ = finish_daily(token, useragent, missionId)
                        if finish_ is not None:
                            code = finish_.get('code')
                            if code == 0:
                                data = finish_.get('data')
                                reward = data.get('reward')
                                print_(f'Task : {name} | Reward : {reward}')
                    else:
                        print_(f"Task : {name} Done")

            #BATAS
            #Get List Task
            time.sleep(2)
            data_list_task = get_task_list(token, useragent)
            if data_list_task is not None:
                print_('Get Task Mission')
                code = data_list_task.get('code', 500)
                if code == 0:
                    data = data_list_task.get('data', {})
                    taskList = data.get('taskList', [])
                    specialTaskList = data.get('specialTaskList', [])
                    for task in taskList:
                        taskStatus = task.get('taskStatus', 0)
                        checkStatus = task.get('checkStatus', 0)
                        taskId = task.get('taskId', '')
                        taskDetail = task.get('taskDetail', '')
                        if checkStatus == 0:
                            time.sleep(2)
                            data_check_status_task = check_task_status(token, useragent, taskId)
                            if data_check_status_task is not None:
                                code = data_check_status_task.get('code', 500)
                                if code == 0:
                                    data = data_check_status_task.get('data', False)
                                    if data:
                                        time.sleep(2)
                                        data_reward_task = claim_reward_task(token, useragent, taskId)
                                        if data_reward_task is not None:
                                            code = data_reward_task.get('code', 500)
                                            if code == 0:
                                                print_(f"Task {taskDetail} Done, Reward {data_reward_task.get('data').get('bonusAmount')}")

                        elif taskStatus == 0:
                            time.sleep(2)
                            data_reward_task = claim_reward_task(token, useragent, taskId)
                            if data_reward_task is not None:
                                code = data_reward_task.get('code', 500)
                                if code == 0:
                                    print_(f"Task {taskDetail} Done, Reward {data_reward_task.get('data').get('bonusAmount')}")
                        
                        else:
                            print_(f"Task {taskDetail} Done")

                    for task in specialTaskList:
                        taskStatus = task.get('taskStatus', 0)
                        checkStatus = task.get('checkStatus', 0)
                        taskId = task.get('taskId', '')
                        taskDetail = task.get('taskDetail', '')
                        if checkStatus == 0:
                            time.sleep(2)
                            data_check_status_task = check_task_status(token, useragent, taskId)
                            if data_check_status_task is not None:
                                code = data_check_status_task.get('code', 500)
                                if code == 0:
                                    data = data_check_status_task.get('data', False)
                                    if data:
                                        time.sleep(2)
                                        data_reward_task = claim_reward_task(token, useragent, taskId)
                                        if data_reward_task is not None:
                                            code = data_reward_task.get('code', 500)
                                            if code == 0:
                                                print_(f"Task {taskDetail} Done, Reward {data_reward_task.get('data').get('bonusAmount')}")

                        elif taskStatus == 0:
                            time.sleep(2)
                            data_reward_task = claim_reward_task(token, useragent, taskId)
                            if data_reward_task is not None:
                                code = data_reward_task.get('code', 500)
                                if code == 0:
                                    print_(f"Task {taskDetail} Done, Reward {data_reward_task.get('data').get('bonusAmount')}")
                        
                        else:
                            print_(f"Task {taskDetail} Done")

            #Check Task Reward
            time.sleep(2)
            data_check_task = get_finish_status_task(token, useragent)
            if data_check_task is not None:
                code = data_check_task.get('code', 500)
                if code == 0:
                    data = data_check_task.get('data')
                    dailyTaskBonusStatus = data.get('dailyTaskBonusStatus')
                    if dailyTaskBonusStatus == 1:
                        time.sleep(2)
                        data_claim_task = claim_bonus_task(token, useragent, 1)
                        if data_claim_task is not None:
                            code = data_claim_task.get('code')
                            if code == 0:
                                print_(f"Claim Daily Task Success, Reward {data_claim_task.get('data').get('bonusAmount')}")

                    commonTaskBonusStatus = data.get('commonTaskBonusStatus')
                    if commonTaskBonusStatus == 1:
                        time.sleep(2)
                        data_claim_task = claim_bonus_task(token, useragent, 2)
                        if data_claim_task is not None:
                            code = data_claim_task.get('code')
                            if code == 0:
                                print_(f"Claim Bonus Task Success, Reward {data_claim_task.get('data').get('bonusAmount')}")
                time.sleep(1)
        #BATAS
        print("KELUAR")
        break
        delay = random.randint(600, 700)
        printdelay(delay)
        time.sleep(delay)
if __name__ == "__main__":
    main()