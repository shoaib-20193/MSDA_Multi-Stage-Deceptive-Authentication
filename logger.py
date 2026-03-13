import datetime
from config import LOG_FILE

def log_event(event_string):
    """Log a general system event with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] EVENT: {event_string}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)

def log_attack(pin_attempt, stage, details=""):
    """Log specific attacker behavior."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] ALERT: Attack detected at {stage}. PIN attempt: '{pin_attempt}'. {details}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)

def log_honeypot_command(command):
    """Log commands executed within the honeypot shell."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] HONEYPOT CMD: {command}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
