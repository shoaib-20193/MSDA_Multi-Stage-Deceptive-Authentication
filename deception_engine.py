import random
from config import REAL_STAGE1_PIN, HONEY_STAGE1_PINS, FALSE_POSITIVE_RATE
from logger import log_attack

def check_stage1(pin):
    """Check if the provided PIN is the real stage 1 PIN."""
    return pin == REAL_STAGE1_PIN

def verify_stage2(pin):
    """Check if the provided PIN is the true stage 2 PIN."""
    from config import REAL_STAGE2_PIN
    return pin == REAL_STAGE2_PIN

def determine_false_positive():
    """Probabilistically determine if a wrong PIN should be falsely accepted."""
    return random.random() < FALSE_POSITIVE_RATE

def detect_honey_pin(pin):
    """Check if the provided PIN is a known honey trap PIN."""
    if pin in HONEY_STAGE1_PINS:
        log_attack(pin, "stage1", "Honey PIN detected.")
        return True
    return False
