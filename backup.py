from netmiko import ConnectHandler
from datetime import datetime

CISCO_ROUTER = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,
}

print(f'Connecting to {CISCO_ROUTER["host"]}...')

try:
    net_connect = ConnectHandler(**CISCO_ROUTER)
    print(f'Successfully connected to {CISCO_ROUTER["host"]}!')

    print("Pulling running configuration. This might take a moment...")
    output = net_connect.send_command('show running-config')

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Router_Backup_{current_time}.txt"

    with open(filename, 'w') as backup_file:
        backup_file.write(output)

    print(f"\nSuccessfully saved running configuration to {filename}!")

    net_connect.disconnect()
    print(f'\nConnection to {CISCO_ROUTER["host"]} closed!')

except Exception as e:
    print(f'Failed to connect to {CISCO_ROUTER["host"]}. Error: {e}')
