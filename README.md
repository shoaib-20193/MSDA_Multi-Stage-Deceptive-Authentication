# Deceptive Multi-Stage Auth Demo

This project is a Python CLI demonstration of a deceptive authentication system. It is designed to combine staged PIN authentication, probabilistic false positives, honey credentials, and a honeypot environment to confuse and monitor brute-force attackers, while allowing legitimate users uninterrupted access.

## What it Covers

- **Attacker Deception:** Implements deceptive strategies to mislead attackers during the authentication process.
- **Probabilistic False Positives:** Simulates false authentication signals by randomly accepting incorrect PINs during the initial stage, wasting the attacker's time.
- **Honey Credentials:** Features trap PINs (honey PINs) that immediately identify an attacker and drop them into a monitored honeypot.
- **Honeypot Environment:** A simulated, fake interactive CLI shell that looks legitimate but serves only to record the attacker's behavior.
- **Attacker Logging:** Centralized logging of all authentication attempts, triggers, and honeypot commands for threat analysis.

## Architecture

The system is built using standard Python libraries and follows a **state-machine** pattern. It consists of the following tightly-coupled modules:

- **`main.py`**: The central CLI entry point that routes the user/attacker based on the state machine's output.
- **`auth_engine.py`**: Controls the core authentication state machine, transitioning between states such as `START`, `REAL_STAGE2`, `FAKE_STAGE2`, `HONEYPOT`, and `REJECT`.
- **`deception_engine.py`**: Houses the probabilistic logic for false positives and the detection logic for honey PINs.
- **`honeypot.py`**: Provides the fake interactive administrative shell environment for trapped attackers.
- **`logger.py`**: Manages centralized logging to `auth_attacks.log`.
- **`config.py`**: Stores all system configurations including credentials, honey PINs, the false-positive rate, and log file paths.

## Running the Demo

1. Clone the repository and navigate to the project directory.
2. Run the application:
   ```bash
   python main.py
   ```
3. Test out different scenarios:
   - **Legitimate Login:** Enter `1234` then `5678`.
   - **Honey PIN:** Enter `0000` to be dropped immediately into the honeypot.
   - **False Positive:** Enter random incorrect PINs to potentially trigger a false Stage 2 prompt to waste time.
   - **Honeypot Interaction:** When in the honeypot (`admin@server:$`), try commands like `ls`, `cat secrets.txt`, `whoami`, or `exit`.
4. Check the `auth_attacks.log` file to observe how your actions were recorded.
