#!/usr/bin/env python3

from typing import Any


def dependencies_comparison() -> dict[str, Any]:

    available: dict[str, Any] = {}

    print("Checking dependencies:")

    try:
        import numpy as np  # type: ignore[import-not-found]
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
        available["numpy"] = np
    except ImportError:
        print("[MISSING] numpy")

    try:
        import pandas as pd  # type: ignore[import-untyped]
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        available["pandas"] = pd
    except ImportError:
        print("[MISSING] pandas")

    try:
        import matplotlib  # type: ignore[import-not-found]
        import matplotlib.pyplot as plt  # type: ignore[import-not-found]
        print(
            f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready"
        )
        available["matplotlib"] = plt
    except ImportError:
        print("[MISSING] matplotlib")

    print()

    return available


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    modules: dict[str, Any] = dependencies_comparison()

    if len(modules) < 3:
        print(
            "Cannot continue. Some dependencies are missing.\n"
            "Advice: Install and activate virtual environment first:\n"
            "   python3 -m venv matrix_env\n"
            "   source matrix_env/bin/activate\n"
            "Install dependencies with one of the following:\n"
            "   pip install -r requirements.txt\n"
            "   poetry install"
        )
        return

    np = modules["numpy"]
    pd = modules["pandas"]
    plt = modules["matplotlib"]

    print("Analyzing Matrix data...\n")

    data = np.random.randint(0, 100, 1000)

    print("Processing 1000 data points...\n")

    df = pd.DataFrame({"robot_age": data})

    mean_val = df["robot_age"].mean()
    max_val = df["robot_age"].max()
    min_val = df["robot_age"].min()

    print(f"    Mean robot age = {mean_val}")
    print(f"    Max robot age = {max_val}")
    print(f"    Min robot age = {min_val}\n")

    print("Generating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(df["robot_age"].values, linewidth=0.8)
    plt.title("Robot Age Analysis")
    plt.xlabel("Robot ID")
    plt.ylabel("Age")

    median = np.median(data)
    plt.axhline(y=median, color='orange', linestyle='--', label='Median')

    max_idx = np.argmax(data)
    min_idx = np.argmin(data)
    plt.scatter(max_idx, data[max_idx], color='green', label='Max')
    plt.scatter(min_idx, data[min_idx], color='red', label='Min')

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
