import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7099251005:AAHEdEdcKreTBYDkIpXmUWytAeLUDS93F64")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20237957"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "966fd23c18752262eba14b80324f49c8")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dipeshmongo72:dipeshmongo72@cluster0.epjfqbx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
