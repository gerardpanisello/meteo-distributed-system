import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--windows', type=int, default=1, help='Number of windows to open')
    parser.add_argument('--start_port', type=int, default=50051, help='Starting port number')
    args = parser.parse_args()

    num_windows = args.windows
    start_port = args.start_port

    # Abrir ventanas del terminal y ejecutar los servidores en puertos consecutivos
    for i in range(num_windows):
        port = start_port + i
        command = f"python3 server_aux.py --port {port}"
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])


