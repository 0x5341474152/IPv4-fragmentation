import socket
import math

def calculate_offset(fragment_number, fragment_sizes):
    offset = 0
    for i in range(fragment_number - 1):
        offset += fragment_sizes[i]
    return offset // 8

def send_fragmented_data(file_path, mtu_size):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 8889)
   
    try:
        client_socket.connect(server_address)
        print("Connected to server.")
    
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()

        print(f"Sending data of size {len(data)} bytes...")

        # Calculate the total number of fragments
        total_fragments = math.ceil(len(data) / mtu_size)

        # Calculate fragment sizes
        fragment_sizes = [mtu_size] * (total_fragments - 1)
        fragment_sizes.append(len(data) - (total_fragments - 1) * mtu_size)

        for i, fragment_size in enumerate(fragment_sizes):
            offset = calculate_offset(i + 1, fragment_sizes)
            identification = 123  # Common identification number for all fragments
            flags = 1 if i < total_fragments - 1 else 0  # Set flag M
            header = f"{identification}/{total_fragments}/{i}/{flags}/{offset}".encode('utf-8')
            fragment_data = data[i * mtu_size: (i + 1) * mtu_size]
            packet = header + b'|' + fragment_data.encode('utf-8')
            client_socket.send(packet)
            print(f"Sent fragment {i + 1} of size {len(fragment_data)} bytes.")

        print("Data sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    print("enter file path and mtu_size->")
    file_path = input("Enter file path: ")
    mtu_size = int(input("Enter MTU size: "))

    send_fragmented_data(file_path, mtu_size)
