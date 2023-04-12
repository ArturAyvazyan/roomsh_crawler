import tomllib

with open("CONFIG.toml", "rb") as f:
    data = tomllib.load(f)
    base_settings = data['base_settings']
    server_settings = data['server_settings']
    redis_settings = data['redis_settings']
    tg_settings = data['tg_settings']

