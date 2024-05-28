import scapy.all as scapy

# Global variables for settings
interface = ""
filter_exp = ""
save_file = "packets.pcap"
local_port = 80

# Function to capture packets
def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_layer = packet.getlayer(scapy.IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto
        return f"{src_ip} -> {dst_ip} (Protocol: {protocol})"
    return "Unknown Packet"

# Function for settings menu
def settings_menu():
    global interface, filter_exp, save_file, local_port
    while True:
        print("\nSettings Menu")
        print("1. Network Interface: " + interface)
        print("2. Filter: " + filter_exp)
        print("3. Save File: " + save_file)
        print("4. Local Port: " + str(local_port))
        print("5. List Available Interfaces")
        print("b. Back to Main Menu")
        choice = input("Select an option to change: ")

        if choice == '1':
            interface = input("Enter Network Interface: ")
        elif choice == '2':
            filter_exp = input("Enter Filter: ")
        elif choice == '3':
            save_file = input("Enter Save File: ")
        elif choice == '4':
            local_port = int(input("Enter Local Port: "))
        elif choice == '5':
            print("\nAvailable Network Interfaces:")
            for iface in scapy.get_if_list():
                print(iface)
        elif choice == 'b':
            break

# Function to start capture
def start_capture():
    global interface, filter_exp, save_file, local_port
    print("\nCapturing on interface " + interface + " with filter '" + filter_exp + "'")
    print("Saving to " + save_file)
    print("Press Ctrl+C to stop capture")

    def packet_handler(packet):
        packet_info = packet_callback(packet)
        print(packet_info)

    # Start sniffing
    try:
        packets = scapy.sniff(iface=interface, filter=filter_exp, prn=packet_handler, store=True)
        scapy.wrpcap(save_file, packets)
    except KeyboardInterrupt:
        print("\nCapture stopped")
    except OSError as e:
        print(f"Error: {e}")

# Main menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Settings")
        print("2. Start Capture")
        print("q. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            settings_menu()
        elif choice == '2':
            start_capture()
        elif choice == 'q':
            break

if __name__ == "__main__":
    main_menu()
