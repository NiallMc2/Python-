'''
UDPServer by: NMG
Listens for packets on a particular address and port.
Alpha: 10NOV2023
'''
import socket
import settings.udp as settings

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Client IP addresses are put into a dictionary so that the details can be extracted in the 'if' statement
client_addr = {
    "CLIENT_UDP1_IPv4": '127.0.0.2',
    "CLIENT_UDP2_IPv4": '127.0.0.3',
    "CLIENT_UDP3_IPv4": '127.0.0.4'
}

print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and begin listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')

def Temp_Alert(WARNING):
    print(f"Temperature: {WARNING}")

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((UDP_IP, UDP_PORT))
        print('Listening on', UDP_IP)
        

        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)
            data = data.decode()
            print(addr, data)
            
            # The IP address is checked to see if it is part of the client_addr dictionary
            if addr[0] in client_addr.values():
                #temperature received from the client is converted to a float and temperature becomes the variable
                temperature = float(data.split()[0])

                # assiging the temperature range
                if temperature < 5 or temperature > 30:

                    # and if temp in that range is received from a device, that has an ip address listed in the client_addr a warning message is sent
                    for device, device_addr in client_addr.items():
                        WARNING = f"Temperature Alert: Rasp Pi {device} - Temperature is {temperature} C"
                        Temp_Alert(WARNING)
                            

                            
            
