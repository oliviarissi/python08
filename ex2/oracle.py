#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv

os → read environment variables
sys → exit safely if needed
dotenv → load .env

🧠 Goal of oracle.py

You are building a program that:

loads config from .env (development)
overrides with real environment variables (production override)
validates missing values
prints a clear “system status” output
🏗️ Clean Structure (what your file should look like)

Think in 5 simple blocks:

1. Imports
2. Load .env
3. Read configuration
4. Validate configuration
5. Display Oracle status


2. Load .env

This is the key step:

load_dotenv()

👉 This loads .env into os.environ


3. Read Configuration

Now you extract variables:

mode = os.getenv("MATRIX_MODE")
db = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion = os.getenv("ZION_ENDPOINT")

4. Apply Defaults + Validation

This is where “Oracle intelligence” happens.

Example logic:
missing = []

Check each:

if not mode:
    mode = "development"

if not db:
    missing.append("DATABASE_URL")

Repeat for others.

Important idea:

.env is optional, not guaranteed

So your program must survive missing values.

7. Security Check Section (important for grading)

You should explicitly check:

no hardcoded secrets
missing values detected
.env used correctly

Example:

print("\nSecurity check:")

if api_key:
    print("[OK] API key loaded from environment")
else:
    print("[WARNING] Missing API key")


Start
 ↓
Load .env file
 ↓
Merge with system environment variables
 ↓
Read config values
 ↓
Fill missing defaults
 ↓
Validate required values
 ↓
Decide dev vs prod behavior
 ↓
Print system status