# eth_account_binary
Generate Ethereum accounts on the fly with a binary.

## Build from source

`pip install pyinstaller`

`pyinstaller --onefile --paths . --add-data "eth_account:eth_account" eth_account_binary.py`

The binary with be placed in the dist directory that's generated during the build process.

### This release file hash

```
sha256sum dist/eth_account_binary 
d9c19b1b4249081f4a9d0fcd35eabf1a2b265135a42e176a20abfe132ff07c7b  dist/eth_account_binary
```
