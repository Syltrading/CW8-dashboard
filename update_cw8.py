import yfinance as yf
import json
from datetime import datetime

ticker = yf.Ticker("CW8.PA")

data = ticker.history(period="1d")

cours = float(data["Close"].iloc[-1])

resultat = {
    "symbole": "CW8.PA",
    "cours": round(cours, 2),
    "date": datetime.now().strftime("%d/%m/%Y %H:%M")
}

with open("cw8.json", "w", encoding="utf-8") as f:
    json.dump(resultat, f, indent=2, ensure_ascii=False)

print(resultat)
