from fastapi import FastAPI , Depends , HTTPException , status
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
import JWT
from datetime import datetime , timedelta
from sqlalchemy import create_engine , column , integer , String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , session

#ایجاد یک محیط رمز نگاری
pwd_context = CryptContext(schemes=["pass"] , deprecated="auto")
secret_key = "my_secret_key"
algorithm = "HS256"
expite_token = 30

