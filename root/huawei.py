from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection

router_ip = '192.168.8.1'
username = 'admin'
password = 'admin'

# PANDUAN BAND
bandsList = [
    ('b1', 'FDD', '2100', '1'),
    ('b2', 'FDD', '1900', '2'),
    ('b3', 'FDD', '1800', '4'),
    ('b4', 'FDD', '1700', '8'),
    ('b5', 'FDD', '850', '10'),
    ('b6', 'FDD', '800', '20'),
    ('b7', 'FDD', '2600', '40'),
    ('b8', 'FDD', '900', '80'),
    ('b19', 'FDD', '850', '40000'),
    ('b20', 'FDD', '800', '80000'),
    ('b26', 'FDD', '850', '2000000'),
    ('b28', 'FDD', '700', '8000000'),
    ('b32', 'FDD', '1500', '80000000'),
    ('b38', 'TDD', '2600', '2000000000'),
    ('b40', 'TDD', '2300', '8000000000'),
    ('b41', 'TDD', '2500', '10000000000'),
]

band = '81' #INPUT MANNUAL # 1 (band 2100) + 80 (band 900) = 81 (keduanya)

connection_url = f'http://{username}:{password}@{router_ip}/'

with AuthorizedConnection(connection_url) as connection:
    client = Client(connection)
    try:
        print(client.device.information())

        # Tampilkan semua data dari net_mode untuk validasi
        print("before")
        print(client.net.net_mode())
        
        print("after")
        client.net.set_net_mode(band, "3FFFFFFF", "03")
        print(client.net.net_mode())
        
    except Exception as e:
        print(f"An error occurred: {e}")