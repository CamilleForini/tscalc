"""Connects to dbsqlite database"""
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME1 = "TS_ongs"
TABLE_NAME2 = "TS_Albuns"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
