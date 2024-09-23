from netmiko import ConnectHandler

import json

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.101',
    'username': 'cisco',
    'password': 'cisco',   
}

connect = ConnectHandler(**cisco_router)
#loopback0 = ["interface loopback 0"]
#configurar = connect.send_config_set(loopback0)
output = connect.send_command("show ip int brief",use_textfsm=True)
formated = json.dumps(output, indent=4)
print(formated) 

