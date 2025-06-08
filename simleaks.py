import json
import subprocess
import sys
import os
from datetime import datetime

def print_trufflehog_summary(json_file="trufflehog_output.json"):
    print("\n=== TruffleHog Summary ===")
    try:
        # TruffleHog outputs one JSON leak per line
        with open(json_file, "r") as f:
            leaks = [json.loads(line) for line in f if line.strip()]

        if not leaks:
            print("No leaks found in TruffleHog report.")
            return

        print(f"Total leaks found: {len(leaks)}\n")
        header = f"{'Leak Type':20} {'File':30} {'Commit':40} {'Author':20} {'Date':20} {'Reason'}"
        print(header)
        print("-" * len(header))

        for leak in leaks:
            leak_type = leak.get('reason', 'N/A')
            file = leak.get('file', 'N/A')
            commit = leak.get('commit', 'N/A')
            author = leak.get('author', 'N/A')
            date = leak.get('date', 'N/A')
            # Try to parse date to readable format
            try:
                date = datetime.fromisoformat(date.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M UTC")
            except Exception:
                pass

            # Show a short reason (truncate if needed)
            reason = leak_type if len(leak_type) < 50 else leak_type[:47] + "..."

            print(f"{reason:20} {file:30} {commit:40} {author:20} {date:20} {reason}")

    except Exception as e:
        print(f"[!] Error reading TruffleHog output: {e}")

def print_gitleaks_summary(json_file="gitleaks_output.json"):
    print("\n=== Gitleaks Summary ===")
    try:
        with open(json_file, "r") as f:
            leaks = json.load(f)  # It's a JSON array

        print(f"Total leaks found: {len(leaks)}")
        for i, leak in enumerate(leaks, 1):
            print(f"\nLeak #{i}:")
            print(f"  File: {leak.get('File', 'N/A')}")
            print(f"  Description: {leak.get('Description', 'N/A')}")
            print(f"  Commit: {leak.get('Commit', 'N/A')}")
            print(f"  StartLine: {leak.get('StartLine', 'N/A')}")
            print(f"  EndLine: {leak.get('EndLine', 'N/A')}")
            print(f"  Secret: {leak.get('Secret', 'N/A')}")
    except Exception as e:
        print(f"[!] Error reading Gitleaks output: {e}")

def run_trufflehog(target_path, output_file="trufflehog_output.json"):
    print("[*] Running TruffleHog scan...")
    cmd = [
        "trufflehog",
        "--json",
        "--regex",
        target_path  # pass the path directly
    ]
    with open(output_file, "w") as f:
        proc = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)

    if proc.returncode == 0 or proc.returncode == 1:
        print(f"[+] TruffleHog output saved to {output_file}")
    else:
        print(f"[!] TruffleHog error: {proc.stderr}")

def run_gitleaks(target_path, output_file="gitleaks_output.json"):
    print("[*] Running Gitleaks scan...")
    cmd = [
        "gitleaks", "detect",
        "--source", target_path,
        "--report-path", output_file,
        "--report-format", "json"
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if proc.returncode == 0 or proc.returncode == 1:
        print(f"[+] Gitleaks output saved to {output_file}")
    else:
        print(f"[!] Gitleaks error: {proc.stderr}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 simleaks.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]

    if not os.path.exists(repo_path):
        print(f"[!] Error: Path '{repo_path}' does not exist.")
        sys.exit(1)

    run_trufflehog(repo_path)
    run_gitleaks(repo_path)

    # Print summaries after running scans
    print_trufflehog_summary()
    print_gitleaks_summary()

if __name__ == "__main__":
    main()
