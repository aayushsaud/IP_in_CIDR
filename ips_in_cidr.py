import ipaddress

# Prompt the user for the CIDR block
cidr = input("Please enter the CIDR block (e.g., 192.168.1.0/24): ")

try:
    # Create an IPv4Network object from the CIDR block
    network = ipaddress.IPv4Network(cidr, strict=False)
    
    # Print each IP address in the network
    for ip in network:
        print(ip)
        
except ValueError as e:
    # Handle invalid CIDR blocks
    print(f"Error: {e}")