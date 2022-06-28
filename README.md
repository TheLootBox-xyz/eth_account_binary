# eth_account_binary
Generate Ethereum accounts on the fly with a binary.

## Build from source

`pip install pyinstaller`

`pyinstaller --onedir --paths . --add-data "eth_account:eth_account" eth_account_binary.py`

The binary with be placed in the dist directory that's generated during the build process.
