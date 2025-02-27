class Settings:
    from environs import Env
    __env = Env()
    __env.read_env()

    BOT_TOKEN = __env('BOT_TOKEN')
    ADMIN_ID = __env('ADMIN_ID')
    DB_API_USERNAME = __env('DB_API_USERNAME')
    DB_API_PASSWORD = __env('DB_API_PASSWORD')
    DB_API_ADDRESS = __env('DB_API_ADDRESS')
    REDIS_HOST = __env('REDIS_HOST')
    REDIS_PASSWORD = __env('REDIS_PASSWORD')
