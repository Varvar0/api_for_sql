from api import DB_api
import pandas as pd
from sqlalchemy import create_engine


with open ('data.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()

data = text[0].split(' ')
engine = create_engine(f'postgresql+psycopg2://{data[1]}:{data[2]}@{data[0]}/{data[3]}')



df = pd.DataFrame([['Earth', 1], ['Moon', 0.606], ['Mars', 0.107]], columns=['name', 'mass_to_earth'])


test = DB_api(engine)