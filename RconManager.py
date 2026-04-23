from rcon.source import Client

def send_command(command, ip, port, password):
    try:
        with Client(ip, int(port), passwd=password) as client:
            return client.run(command)
    except Exception as e:
        return f"Error: {e}"