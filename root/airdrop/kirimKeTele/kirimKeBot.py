import os
import requests

# Konfigurasi
token = 'MASUKKAN TOKEN BOT DISINI'  
chat_id = 'MASUKKAN CHATID DISINI'  

# URL API Telegram untuk mengirim pesan
url = f'https://api.telegram.org/bot{token}/sendMessage'

# Fungsi untuk mengirim pesan ke Telegram
def send_message(file_content, file_name):
    nama_file = file_name.split("_")[1].split(".")[0].upper()
    data = {
        'chat_id': chat_id,
        'text': f"---- {nama_file} ----\n{file_content}"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f'{nama_file} berhasil dikirim')
    else:
        print(f'{nama_file} Gagal! | ', response.text)

# Path ke direktori dengan file log
log_directory = '/root/airdrop/LOG'

# Baca dan kirim isi setiap file log
for file_name in os.listdir(log_directory):
    if file_name.endswith('.log') and file_name != "LOG_kirim.log":
        file_path = os.path.join(log_directory, file_name)
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                send_message(file_content, file_name)
        except Exception as e:
            print(f'Error saat membaca atau mengirim pesan dari {file_name}: {e}')
