import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URI: postgresql://username:password@host.port/database

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
print(config.read(file_config))

print(file_config)


URI = f"postgresql://posgres:123456@localhost:5432/HW7"