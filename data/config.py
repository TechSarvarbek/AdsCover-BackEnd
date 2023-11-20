from environs import Env

env = Env()
env.read_env()



EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
SECRET_KEY = env.str("SECRET_KEY")