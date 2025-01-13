from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import Table, MetaData, Column, String, JSON, DateTime, inspect
from sqlalchemy.exc import SQLAlchemyError
from app.models.database import db
from dotenv import load_dotenv
import os 

load_dotenv()

table_name = os.getenv('TABLE_NAME')

def generate_uuid():
   return str(uuid4())

metadata = MetaData()

data = Table(
   table_name, metadata,
   Column('id', String(36), primary_key=True, default=generate_uuid),
   Column('method', String(10), nullable=False),
   Column('endpoint', String(50), nullable=False), 
   Column('headers', JSON),
   Column('body', JSON),
   Column('timestamp', DateTime(timezone=True), default=lambda: datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S%z'))
)

def save_request_data(method, endpoint, headers, body):
   try:
       with db.engine.connect() as conn:
           if not inspect(db.engine).has_table(table_name):
               metadata.create_all(db.engine)
           
           conn.execute(data.insert().values(
               method=method,
               endpoint=endpoint,
               headers=headers,
               body=body
           ))
           conn.commit()
       return True, "Data saved successfully"
   except SQLAlchemyError as e:
       return False, str(e)