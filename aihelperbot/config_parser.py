import toml


with open("config.toml", "r", encoding="utf-8") as config_file:
    config = toml.load(config_file)
