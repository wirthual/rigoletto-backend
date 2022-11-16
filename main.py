from fastapi_csv import FastAPI_CSV
from fastapi.middleware.cors import CORSMiddleware

CSV_URL = "https://webrigoletto.uba.de/Rigoletto/Home/GetClassificationFile/Export_Tabelle"

origins = [
    "*"
]


app = FastAPI_CSV(CSV_URL,delimiter='|')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
)