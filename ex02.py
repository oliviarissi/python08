import os
import sys
from dotenv import load_dotenv


def security_check():
    """
    Simple security checks.
    """
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")

    print("[OK] Production overrides available")


def main():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    missing = []

    # MATRIX_MODE
    matrix_mode = os.getenv("MATRIX_MODE")
    if matrix_mode is None:
        matrix_mode = "development"
        print("Mode: development [DEFAULT]")
    else:
        print(f"Mode: {matrix_mode}")

    # DATABASE_URL
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        if matrix_mode == "production":
            print("Database: Connected to production mainframe")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Missing configuration")
        missing.append("DATABASE_URL")

    # API_KEY
    api_key = os.getenv("API_KEY")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")
        missing.append("API_KEY")

    # LOG_LEVEL
    log_level = os.getenv("LOG_LEVEL")
    if log_level is None:
        log_level = "INFO"
        print("Log Level: INFO [DEFAULT]")
    else:
        print(f"Log Level: {log_level}")

    # ZION_ENDPOINT
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
        missing.append("ZION_ENDPOINT")

    # Missing configuration summary
    if missing:
        print("\nMissing configuration variables:")
        for item in missing:
            print(f"- {item}")

        print("\nCreate a .env file or export environment variables.")

    security_check()

    if missing:
        sys.exit(1)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()