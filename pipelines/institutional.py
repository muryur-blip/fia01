def get_institutional_holders(symbol: str) -> dict:
    """
    Fetch institutional holders from Nasdaq API.
    Returns top holders if available.
    """

    url = f"https://api.nasdaq.com/api/company/{symbol}/institutional-holdings"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if not data or "data" not in data or data["data"] is None:
            return {"symbol": symbol, "holders": [], "message": "No institutional data found"}

        holders = data["data"].get("institutionalHolders", [])

        cleaned = []
        for h in holders[:5]:  # Only top 5
            cleaned.append({
                "holder": h.get("entityProperName"),
                "shares": h.get("sharesHeld"),
                "change_pct": h.get("pctChange"),
                "report_date": h.get("reportDate")
            })

        return {"symbol": symbol, "holders": cleaned}

    except Exception as e:
        return {"symbol": symbol, "error": str(e)}
