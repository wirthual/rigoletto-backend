from fastapi_csv import FastAPI_CSV

CSV_URL = "https://webrigoletto.uba.de/Rigoletto/Home/GetClassificationFile/Export_Tabelle"

app = FastAPI_CSV(CSV_URL,delimiter='|')