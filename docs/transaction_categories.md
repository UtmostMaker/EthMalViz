# Malicious Transaction Taxonomy

## 1. Phishing Transactions
- **Indicators**: 
  - `input_data` contains known phishing URLs
  - Associated with flagged addresses from [Chainabuse](https://www.chainabuse.com/)
  - Example: 0x4e5f2F4c... (Fake MetaMask address)

## 2. Scam Contracts
- **Indicators**:
  - HoneyPot contracts
  - Rug pull patterns
  - Verified contracts with 0x0000... metadata
  - Source: [Etherscan Verified Contracts Abuse](https://etherscan.io/labelcloud)

## 3. Mixer Transactions
- **Indicators**:
  - Direct interactions with Tornado Cash (0x1c7...)
  - Cyclic transaction patterns
  - Threshold: ≥ 1 ETH mixed
