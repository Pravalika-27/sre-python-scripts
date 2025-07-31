import socket

def check_port(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"✅ {host}:{port} is open")
    except:
        print(f"❌ {host}:{port} is not reachable")

check_port("example.com", 80)
