# scripts/data_collection/fetch_blocklists.py
import requests
from pathlib import Path

# Configure paths
DATA_DIR = Path(__file__).parent.parent.parent / "data/external/blocklists"
DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

# Blocklist sources
SOURCES = {
    "urls_darklist": "https://raw.githubusercontent.com/MyEtherWallet/ethereum-lists/master/src/urls/urls-darklist.json",
    "addresses_darklist": "https://raw.githubusercontent.com/MyEtherWallet/ethereum-lists/master/src/addresses/addresses-darklist.json"
}


def fetch_blocklists():
    """Fetch and save predefined blocklists from public repositories."""
    for name, url in SOURCES.items():
        print(f"Fetching {name}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        
        output_path = DATA_DIR / f"{name}.json"
        with open(output_path, "w") as f:
            f.write(response.text)
        print(f"Saved to {output_path}")

if __name__ == "__main__":
    fetch_blocklists()
