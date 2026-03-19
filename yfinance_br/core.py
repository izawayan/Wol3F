# Arquivo: yfinance_br/core.py
import yfinance as yf
import pandas as pd
from datetime import datetime
import warnings

def download_seguro(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Baixa dados do yfinance e avisa se o ativo foi deslistado antes da data final.
    """
    df = yf.download(ticker, start=start, end=end, progress=False)

    if df.empty:
        warnings.warn(f"Nenhum dado encontrado para {ticker}.")
        return df

    last_valid_date = df.index[-1].date()
    requested_end_date = datetime.strptime(end, "%Y-%m-%d").date()

    # Se faltam mais de 7 dias entre o último dado e a data pedida, foi deslistada/suspensa
    days_missing = (requested_end_date - last_valid_date).days
    
    if days_missing > 7:
        warnings.warn(
            f"\n🚨 ALERTA DE DELISTING/SUSPENSÃO: {ticker}\n"
            f"O último dado real foi em {last_valid_date}.\n"
            f"Faltam {days_missing} dias para cobrir o período solicitado."
        )

    return df