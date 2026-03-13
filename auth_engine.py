from deception_engine import check_stage1, determine_false_positive, detect_honey_pin, verify_stage2
from logger import log_event, log_attack

# States
START = "START"
REAL_STAGE2 = "REAL_STAGE2"
FAKE_STAGE2 = "FAKE_STAGE2"
HONEYPOT = "HONEYPOT"
REJECT = "REJECT"

def stage1_auth(pin):
    """
    Process stage 1 authentication.
    Returns the next state.
    """
    if detect_honey_pin(pin):
        return HONEYPOT
    
    if check_stage1(pin):
        log_event("Stage 1 success (Real)")
        return REAL_STAGE2
    
    if determine_false_positive():
        log_attack(pin, "stage1", "False positive triggered.")
        return FAKE_STAGE2
        
    log_attack(pin, "stage1", "Failed attempt, rejected.")
    return REJECT

def stage2_auth(pin, state):
    """
    Process stage 2 authentication.
    Returns the final outcome state.
    """
    if state == REAL_STAGE2:
        if verify_stage2(pin):
            log_event("Stage 2 success. Full authentication granted.")
            return "SUCCESS"
        else:
            log_attack(pin, "stage2", "Failed stage 2 after successful stage 1.")
            return REJECT
            
    elif state == FAKE_STAGE2:
        # Any PIN entered here is a trapped attacker
        log_attack(pin, "stage2", "Trapped attacker entered PIN during FAKE_STAGE2.")
        return HONEYPOT
        
    return REJECT
