import requests
from models import InstitutionalData, HolderChange

def get_institutional_holders(symbol: str):
    url = f"https://api.nasdaq.com/api/company/{symbol}/institutional-holdings"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if not data or "data" not in data or not data["data"]:
            return None

        # 1) Birincil kaynak
        holders = data["data"].get("institutionalHolders")

        # 2) Alternatif kaynak (Nasdaq bazen sadece burayı dolduruyor)
        if not holders:
            holders = data["data"].get("ownershipSummary", {}).get("rows", [])

        if not holders:
            return None

        top = []
        for h in holders[:5]:
            top.append(
                HolderChange(
                    name=h.get("holderName") or h.get("entityProperName"),
                    position=h.get("sharesHeld") or h.get("position"),
                    change_pct=h.get("pctChange") or h.get("changePercent"),
                    filing_date=h.get("reportDate") or h.get("filedDate"),
                    meta={"source": "Nasdaq API"}
                )
            )

        return InstitutionalData(top_holders=top, hedge_fund_activity=[])

    except Exception as e:
        print("Institutional error:", e)
        return None

