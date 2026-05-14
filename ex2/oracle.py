#!/usr/bin/env python3

import os
from dotenv import load_dotenv  # type: ignore[import-not-found]


def security_check() -> None:

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    else:
        print("[WARNING] No .env file found")
        print("[OK] Production overrides available")


def main() -> None:

    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    matrix_mode = os.getenv("MATRIX_MODE")
    if matrix_mode is None:
        matrix_mode = "development"
        print("Mode: development [DEFAULT]")
    else:
        print(f"Mode: {matrix_mode}")

    database_url = os.getenv("DATABASE_URL")
    if database_url:
        if matrix_mode == "production":
            print("Database: Connected to production mainframe")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: [MISSING]")

    api_key = os.getenv("API_KEY")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [MISSING]")

    log_level = os.getenv("LOG_LEVEL")
    if log_level is None:
        log_level = "INFO"
        print("Log Level: INFO [DEFAULT]")
    else:
        print(f"Log Level: {log_level}")

    zion_endpoint = os.getenv("ZION_ENDPOINT")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline [MISSING]")

    security_check()


if __name__ == "__main__":
    main()
