"""
Configuration for Deceptive Multi-Stage Authentication Demo.
"""

REAL_STAGE1_PIN = "1234"
REAL_STAGE2_PIN = "5678"

# PINs that instantly flag the user as an attacker and drop them in the honeypot
HONEY_STAGE1_PINS = ["0000", "1111", "9999", "4321"]

# Probability (0.0 to 1.0) that a wrong stage 1 PIN will be falsely accepted
# to lead the attacker into stage 2 and waste their time.
FALSE_POSITIVE_RATE = 0.3

# File to log attacker behavior and general system events
LOG_FILE = "auth_attacks.log"
