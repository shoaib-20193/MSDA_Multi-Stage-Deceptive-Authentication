import time
import sys
from logger import log_honeypot_command

def launch_honeypot():
    """
    Launch a fake interactive CLI environment for trapped attackers.
    This simulates a shell but actually does nothing except log their commands.
    """
    print("\n--- System Authentication Successful ---")
    print("Welcome to Admin Console v2.1")
    print("Type 'help' for a list of commands, or 'exit' to disconnect.\n")
    
    log_honeypot_command("SESSION_STARTED")
    
    while True:
        try:
            command = input("admin@server:$ ").strip()
            if not command:
                continue
                
            log_honeypot_command(command)
            
            if command == "exit":
                print("Disconnecting...")
                time.sleep(1)
                break
            elif command == "ls":
                print("secrets.txt  passwords.db  system_logs")
            elif command.startswith("cat secrets.txt"):
                print("AWS_KEY=AKIAIOSFODNN7EXAMPLE")
                print("AWS_SECRET=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
                print("DB_PASS=Sup3rS3cr3t!")
            elif command.startswith("cat passwords.db"):
                print("Binary file passwords.db matches")
            elif command == "whoami":
                print("admin")
            elif command == "help":
                print("Available commands: ls, cat, whoami, help, exit")
            else:
                print(f"bash: {command.split()[0]}: command not found")
                
        except (KeyboardInterrupt, EOFError):
            print("\nDisconnecting...")
            log_honeypot_command("SESSION_TERMINATED_ABRUPTLY")
            break
