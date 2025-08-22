import socket

'''
The following class is for communicating to Keyence KV PLC device.

Basically is an implementation of the socket module by using the PLC
expected ASCII commands to read and write the PLC device memory.

Class is limited to the following device memory areas: R, MR and DM.

Class contains the following methods:

    1. read() -> read a single device (PLC memory addresses)
    2. write() -> write a single device (PLC memory address)
    3. multi_read() -> read multiple (same type) devices (PLC memory addresses)
    4. multi_write() -> write multiple (same type) devices (PLC memory addresses)

Implementation example:

# Instance some plc connections
plc1 = kv_plc_tcp_socket('192.168.0.1', 8080, timeout=5)
plc2 = kv_plc_tcp_socket('192.168.0.2', 8080)
plc3 = kv_plc_tcp_socket('192.168.0.3', 8000, timeout=2)

plc1.multi_read(MR, 5000, 20)
plc2.read(MR, 3100)
plc3.multi_write(MR, 6032, data_list) # multi_write() method infers the number of devices to be written from the data list parameter length
plc1.write(DM, 101, data)

'''
class kv_plc_tcp_socket:
    def __init__(self, ipv4_address: str, port_number: int, timeout: int | None = None):
        self.__valid_devices = ('R', 'MR', 'DM')
        self.__address = ipv4_address
        self.__port_number = port_number

        if timeout == None:
            self.__timeout = 3
        else:
            self.__timeout = timeout

    def read(self, device: str, device_number: int) -> int:
        # Check that device matches one of the supported by the class
        if device not in self.__valid_devices:
            raise ValueError(f'Unsupported device type {device}')

        with socket.create_connection((self.__address, self.__port_number), timeout=self.__timeout) as s:
            s.sendall(f'RD {device}{device_number}\r'.encode('ascii'))
            server_response = s.recv(1024)

        # Check for empty response before decoding
        if server_response == b'':
            raise Exception('Connection closed by peer')
        
        # Decode and strip successfully receive message
        buffer_value = server_response.decode('ascii').strip()

        match device:
            case 'R':
                return bool(int(buffer_value))
            case 'MR':
                return bool(int(buffer_value))
            case 'DM':
                return int(buffer_value)
            case _:
                raise ValueError(f'Unsupported device type {device}')
            
    def write(self, device: str, device_number: int, data: bool | int):
        # Check that device parameter matches one of the supported by the class
        if device not in self.__valid_devices:
            raise ValueError(f'Unsupported device type {device}')
        
        #Check that data matches the device type
        match device:
            case 'R':
                if not(type(data) == bool or type(data) == int):
                    raise ValueError(f'Unsupported device value, {device} data value must match bool class or int class with a value of 0 or 1')
                elif type(data) == int and not(data == 0 or data == 1):
                    raise ValueError(f'Unsupported device value, {device} with data int class must have a value of 0 or 1')
            case 'MR':
                if not(type(data) == bool or type(data) == int):
                    raise ValueError(f'Unsupported device value, {device} data value must match bool class or int class with a value of 0 or 1')
                elif type(data) == int and not(data == 0 or data == 1):
                    raise ValueError(f'Unsupported device value, {device} with data int class must have a value of 0 or 1')
            case 'DM':
                if type(data) != int:
                    raise ValueError(f'Unsupported device value, {device} data value must match int class')
                elif type(data) == int and not (0 <= data <= 65535):
                    raise ValueError(f'Unsupported device value, {device} with data value {data} is out of range')
        
        # Process the value to be sent accordingly to the data type of the data parameter
        if type(data) == bool:
            value = str(int(data))
        elif type(data) == int:
            value = str(data)

        with socket.create_connection((self.__address, self.__port_number), timeout=self.__timeout) as s:
            s.sendall(f'WR {device}{device_number} {value}\r'.encode('ascii'))
            # Wait for server response just to take out the message from the socket buffer
            server_response = s.recv(1024)

        if server_response == b'':
            raise Exception('Connection closed by peer')
        
    def multi_read(self, device: str, device_number: int, number_of_devices: int) -> list[int]:
        # Check that device matches one of the supported by the class
        if device not in self.__valid_devices:
            raise ValueError(f'Unsupported device type {device}')
        
        list_of_values = []

        for i in range(0, number_of_devices):
            list_of_values.append(self.read(device, device_number + i))

        return list_of_values

    def multi_write(self, device: str, device_number: int, data_list: list[int]):
        # Check that device matches one of the supported by the class
        if device not in self.__valid_devices:
            raise ValueError(f'Unsupported device type {device}')
        
        # Infer the number of devices to be written from the data list length
        number_of_devices = len(data_list)
        
        for i in range(0, number_of_devices):
            self.write(device, device_number + i, data_list[i])