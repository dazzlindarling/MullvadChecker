# 🔑 Mullvad Key Checker

This project allows you to quickly check the validity of multiple Mullvad VPN keys via the official API, identify valid keys, and generate a file containing only the valid ones.

## 🚀 Features
- Automatically checks all keys listed in a text file
- Automatically removes duplicate keys
- Customizable delay between each request to avoid rate limiting
- Saves valid keys in a separate file (`validsXXXXXX.txt`)

## 📦 Requirements
- Python 3.7+
- Modules: `requests`, `colorama`,`pystyle`

Install dependencies with:
```bash
pip install -r requirements.txt
```

## 📝 Usage
1. Put all your Mullvad keys (one per line) in a text file, e.g. `keys.txt`.
2. Run the checker script:
   ```bash
   python main.py
   ```
   > By default, the script reads from `keys.txt`.

3. At the end, valid keys will be saved in a file like `valids123456.txt`.

## ⚙️ Customization
- **Delay between requests**: Change the value of `time.sleep(0.7)` in the script to adjust the delay (in seconds).
- **Input file name**: Change the `file` variable at the top of the script if needed.

## 🖥️ Example Output
```
OK - 1337567890123456 - 82days left
INVALID - 1234567890123456 - 404
Valid keys saved in valids123456.txt
```

## 🛡️ Tips
- Respect the delay between requests to avoid being temporarily blocked by the Mullvad API.
- Never share your Mullvad keys publicly!

## ✨ Contact
- Discord: dazzlindarling


---
## ❤️ Donation
- LTC: LY1LAYAYyGu2Tx6XFKmBSBxBUo8SQ4QCp4
- BTC: bc1qk5mx9c3af0kxskc2uyt2004mhk8rgnllll266a
- ETH: 0xD1FBd6CF494E6b7fb38863eD56B005A95e41079A


