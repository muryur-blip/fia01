import yfinance as yf

def get_financials(symbol: str) -> dict:
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        return {
            "symbol": symbol,
            "revenue_ttm": info.get("totalRevenue"),
            "revenue_quarter": info.get("revenueQuarterlyGrowth"),
            "net_income": info.get("netIncomeToCommon"),
            "eps": info.get("trailingEps"),
            "pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "ps": info.get("priceToSalesTrailing12Months"),
            "peg": info.get("pegRatio"),
            "total_debt": info.get("totalDebt"),
            "de_ratio": info.get("debtToEquity"),
            "free_cash_flow": info.get("freeCashflow"),
        }

    except Exception as e:
        return {"symbol": symbol, "error": str(e)}
