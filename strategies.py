from abc import ABC, abstractmethod
from data_loader import MarketDataPoint

class Strategy(ABC):
    @abstractmethod
    def GenerateSignals(self, tick: MarketDataPoint) -> list:
        pass
    
class Strategy1(Strategy):
    def GenerateSignals(self, tick: MarketDataPoint) -> list:
        pass