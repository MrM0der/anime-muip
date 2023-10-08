import requests
import hashlib
import urllib.parse

def sha256_sign(secret, message):
    sha256 = hashlib.sha256()
    sha256.update(f"{message}{secret}".encode())
    return sha256.hexdigest()

def muip_client(uid: str, command: str, secret: str, ticket: str = "GM", region: str = "dev_docker", url: str = "http://127.0.0.1:21051/api", cmd_id: str = "1116"):

    payload = {
        "region": region,
        "ticket": ticket,
        "cmd": cmd_id,
        "uid": uid,
        "msg": command
    }

    kvs = []
    for key, value in payload.items():
        kvs.append(f"{key}={value}")
    kvs.sort()

    qstr = "&".join(kvs)
    sign = sha256_sign(secret, qstr)

    params = {
        "region": region,
        "ticket": ticket,
        "cmd": cmd_id,
        "uid": uid,
        "msg": command,
        "sign": sign
    }

    response = requests.get(url, params=params)
    return response.content.decode()
