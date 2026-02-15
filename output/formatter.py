def format_report(financials, institutional) -> str:
    """
    Combine financial and institutional data into a clean text report.
    """

    # -----------------------------
    # FINANCIAL SECTION
    # -----------------------------
    if financials is None:
        return "No financial data available.\n"

    symbol = getattr(financials, "symbol", "N/A")

    fin_section = f"""
==============================
  FINANCIAL OVERVIEW — {symbol}
==============================

Revenue (TTM):        {financials.revenue_ttm}
Quarterly Growth:     {financials.revenue_quarter}
Net Income:           {financials.net_income}
EPS (Trailing):       {financials.eps}
P/E (Trailing):       {financials.pe}
Forward P/E:          {financials.forward_pe}
Price/Sales (TTM):    {financials.ps}
PEG Ratio:            {financials.peg}
Total Debt:           {financials.total_debt}
Debt/Equity:          {financials.de_ratio}
Free Cash Flow:       {financials.free_cash_flow}
"""

    # -----------------------------
    # INSTITUTIONAL SECTION
    # -----------------------------
    inst_section = f"""
==============================
  INSTITUTIONAL HOLDERS — {symbol}
==============================
"""

    if institutional is None or not institutional.top_holders:
        inst_section += "No institutional holder data available.\n"
    else:
        for h in institutional.top_holders:
            inst_section += (
                f"\nHolder:       {h.name}"
                f"\nShares Held:  {h.position}"
                f"\nChange (%):   {h.change_pct}"
                f"\nReport Date:  {h.filing_date}\n"
            )

    return fin_section + "\n" + inst_section

