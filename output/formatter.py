def format_report(financials: dict, institutional: dict) -> str:
    """
    Combine financial and institutional data into a clean text report.
    """

    symbol = financials.get("symbol", "N/A")

    # --- Financial Section ---
    fin_section = f"""
==============================
  FINANCIAL OVERVIEW — {symbol}
==============================

Revenue (TTM):        {financials.get("revenue_ttm")}
Quarterly Growth:     {financials.get("revenue_quarter")}
Net Income:           {financials.get("net_income")}
EPS (Trailing):       {financials.get("eps")}
P/E (Trailing):       {financials.get("pe")}
Forward P/E:          {financials.get("forward_pe")}
Price/Sales (TTM):    {financials.get("ps")}
PEG Ratio:            {financials.get("peg")}
Total Debt:           {financials.get("total_debt")}
Debt/Equity:          {financials.get("de_ratio")}
Free Cash Flow:       {financials.get("free_cash_flow")}
"""

    # --- Institutional Section ---
    holders = institutional.get("holders", [])
    inst_section = f"""
==============================
  INSTITUTIONAL HOLDERS — {symbol}
==============================
"""

    if not holders:
        inst_section += "No institutional holder data available.\n"
    else:
        for h in holders:
            inst_section += (
                f"\nHolder:       {h.get('holder')}"
                f"\nShares Held:  {h.get('shares')}"
                f"\nChange (%):   {h.get('change_pct')}"
                f"\nReport Date:  {h.get('report_date')}\n"
            )

    # Final combined report
    return fin_section + "\n" + inst_section
