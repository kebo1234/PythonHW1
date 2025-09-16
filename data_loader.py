import csv
import time
import random
import datetime
from dataclasses import dataclass

@dataclass(frozen = True)
class MarketDataPoint:
    timestamp: datetime.datetime
    symbol: str
    price: float
    
def ReadMarketCSV(filename):
    MarketData = list()
    with open(filename, 'r', newline = '') as f:
        CsvReader = csv.reader(f)
        next(CsvReader)  # Skip header row
        for row in CsvReader:
            timestamp = datetime.datetime.fromisoformat(row[0])
            symbol = row[1]
            price = float(row[2])
            MarketData.append(MarketDataPoint(timestamp, symbol, price))
    return MarketData