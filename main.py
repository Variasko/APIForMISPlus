from fastapi import FastAPI
from random import *
from datetime import *

# необходимые библиотеки
# pip install "fastapi[all]"
# pip install "uvicorn[standart]"

"""
как запустить:
 1. установить все необходимые бибилиотеки
 2. в терминале напсиать uvicorn main:app --reload
 3. использовать код из request.py(запустить)
"""

app = FastAPI()

kabs = [x for x in range(22)]  # порядковые номера кабинетов (без регистратуры)
inOut = ["in", 'out']
docs = [x for x in range(10)]  # id докторов (подтянуть из бд)
pats = [x for x in range(10)]  # id пациента (подтянуть из бд)
pers = [docs, pats]  # для рандомности


@app.get("/")
def read_root():
    userGroup = choice(pers)
    user = choice(userGroup)
    if userGroup == pers[0]:
        code = 1
    else:
        code = 2

    mess = {

        "PersonCode": user,
        "PersonalRole": code,
        "LastSecurityPointNumber": choice(kabs),
        "LastSecurityPointDirection": choice(inOut),
        "LastSecurityPointTime": datetime.now()
    }
    return mess
