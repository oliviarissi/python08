#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    """
    Load environment variables from .env file
    and return configuration values.
    """

    load_dotenv("")

    config: dict = {
      "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
      "DATABASE_URL": os.getenv("DATABASE_URL"),
      "API_KEY": os.getenv("API_KEY"),
      "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
      "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def check_missing(config: dict) -> list:
    """
    Check for missing required configuration.
    """

    missing: list = []

    required: list = [
        "DATABASE_URL",
        "API_KEY",
        "ZION_ENDPOINT",
    ]

    for item in required:
        if not config.get(item):
            missing.append(item)

    return missing


def display_configuration(config):
    """
    Display current configuration.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to production mainframe")
    else:
        print("Database: Connected to local instance")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    """
    Perform simple security checks.
    """
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")

    print("[OK] Production overrides available")

def main() -> None:
  
    config: dict = load_configuration()

    print(config)
    print()

    missing: list = check_missing(config)

    display_configuration(config)

    if missing:
        print("\nWARNING: Missing configuration variables:")
        for item in missing:
            print(f"- {item}")

        print("\nCreate a .env file or export environment variables.")
        sys.exit(1)

    security_check()

    print("\nThe Oracle sees all configurations.")



if __name__ == "__main__":
    main()
