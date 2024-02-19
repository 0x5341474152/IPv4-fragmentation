
import socket

def reassemble_data(received_data):
    fragments = {}
    for packet in received_data:
        header, fragment = packet.split(b'|', 1)
        identification, total_fragments, fragment_number, flags, offset = map(int, header.split(b'/'))
        fragments[fragment_number] = fragment

    data = b"".join(fragments[i] for i in range(total_fragments))
    return data, identification, flags, offset

def receive_fragmented_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 8889)
    server_socket.bind(server_address)

    print("Server is listening for incoming fragments...")

    received_data = []
    total_fragments = None 
    while True:
        packet, client_address = server_socket.recvfrom(1024)
        header, fragment = packet.split(b'|', 1)
        identification, total_fragments, fragment_number, flags, offset = map(int, header.split(b'/'))
        received_data.append(packet)

        # creation of files for each fragment
        with open(f"fragment_{fragment_number}.txt", "wb") as file:
            file.write(fragment)

        # Display identification, flags, offset, and size of data received in each fragment
        fragment_size = len(fragment)
        print(f"Fragment {fragment_number + 1}/{total_fragments} - Identification: {identification}, M: {flags}, Offset: {offset}, Size: {fragment_size} bytes")

        # Reassemble data when all fragments are received
        if len(received_data) == total_fragments:
            data, identification, flags, offset = reassemble_data(received_data)
            print(f"\nReassembled Data: {data.decode()} Size: {len(data)} bytes")
            print(f"Identification: {identification}, More_fragment: {flags}, Offset: {offset}")

            break

    server_socket.close()

if __name__ == "__main__":
    receive_fragmented_data()
