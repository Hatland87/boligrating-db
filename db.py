import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv('ROOT_PASSWORD')
)
cursor = cnx.cursor()