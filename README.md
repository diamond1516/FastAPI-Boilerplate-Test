# FastAPI Boilerplate

## Getting Started

Setup project environment with [virtualenv](https://pypi.org/project/virtualenv/) and [pip](https://pypi.org/project/pip/).


```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cp .env.example .env
$ mkdir -p keys
$ openssl genpkey -algorithm RSA -out keys/private_key.pem -pkeyopt rsa_keygen_bits:2048
$ openssl rsa -pubout -in keys/private_key.pem -out keys/public_key.pem
```
