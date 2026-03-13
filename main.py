import sys
import time
from auth_engine import stage1_auth, stage2_auth, START, REAL_STAGE2, FAKE_STAGE2, HONEYPOT, REJECT
from honeypot import launch_honeypot
from logger import log_event

#This file is the main entry point of the application
def print_slow(text, delay=0.03):
    """Print text character by character for a nice CLI effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print_slow("Initializing Multi-Stage Authentication System...")
    log_event("Application startup")
    
    #Stage 1 Authentication
    print("\n[Stage 1] Authentication Required")
    stage1_pin = input("Enter Stage 1 PIN: ").strip()
    
    state = stage1_auth(stage1_pin)
    
    if state == HONEYPOT:
        launch_honeypot()
        return
        
    if state == REJECT:
        print_slow("Authentication Failed. Access Denied.")
        return

    #Stage 2 Authentication    
    print("\n[Stage 2] Additional Authentication Required")
    time.sleep(0.5)
    stage2_pin = input("Enter Stage 2 PIN: ").strip()
    
    final_outcome = stage2_auth(stage2_pin, state)
    
    if final_outcome == "SUCCESS":
        print_slow("Authentication Complete. Welcome.")
        log_event("User granted access to standard functionality.")
        print("\n[System Ready - Real Access Granted]")
        
    elif final_outcome == HONEYPOT:
        print_slow("Verifying credentials...")
        time.sleep(1)
        launch_honeypot()
        
    else:
        print_slow("Authentication Failed. Access Denied.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting.")
