# scripts/data_collection/fetch_transactions.py
import os, json, re
from pathlib import Path
from dotenv import load_dotenv
from etherscan import Etherscan

# Load environment
load_dotenv()
ETH = Etherscan(os.getenv("ETHERSCAN_API_KEY"))

# Paths
BASE_DIR        = Path(__file__).parent.parent.parent
BLOCKLIST_DIR   = BASE_DIR / "data/external/blocklists"
RAW_TX_DIR      = BASE_DIR / "data/raw/transactions"
RAW_TX_DIR.mkdir(parents=True, exist_ok=True)

# Regex to validate Ethereum addresses
ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")

def load_addresses(file_path):
    """
    Return only valid Ethereum addresses from the given JSON file.
    """
    with open(file_path) as f:
        data = json.load(f)

    valid = []
    for item in data:
        # If it's a string and matches address pattern
        if isinstance(item, str) and ADDRESS_RE.match(item):
            valid.append(item)
        # If it's a dict with an 'address' field
        elif isinstance(item, dict):
            addr = item.get("address")
            if isinstance(addr, str) and ADDRESS_RE.match(addr):
                valid.append(addr)
    return valid

def fetch_and_save(address):
    """
    Fetch normal transactions for one address and save as JSON.
    """
    try:
        txs = ETH.get_normal_txs_by_address(
            address, startblock=0, endblock=99999999, sort="asc"
        )
    except Exception as e:
        print(f"Error fetching {address}: {e}")
        return

    out_file = RAW_TX_DIR / f"{address}.json"
    out_file.write_text(json.dumps(txs))
    print(f"Saved {len(txs)} txs for {address}")

def main():
    """
    Iterate only over blocklist files whose name contains 'address'.
    """
    for blk_file in BLOCKLIST_DIR.glob("*address*.json"):
        addrs = load_addresses(blk_file)
        print(f"Processing {blk_file.name} ({len(addrs)} addresses)")
        for addr in addrs:
            fetch_and_save(addr)

if __name__ == "__main__":
    main()
