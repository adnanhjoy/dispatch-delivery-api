import jwt
def access_token_generate(payload:dict):
    return jwt.encode(payload, "secret", algorithm="HS256")