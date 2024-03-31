from dotenv import load_dotenv
import os
import time
import jwt

load_dotenv()
api_key = os.getenv('API_KEY')
# 假设 15s 过期
exp_seconds = 15

def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)

    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )

print(generate_token(api_key, exp_seconds))