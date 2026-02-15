def format_report(financials, institutional) -> str:
    """
    Combine financial and institutional data into a clean text report.
    Supports both dict and dataclass inputs.
    """

    # -----------------------------
    # FINANCIAL SECTION
    # -----------------------------
    if financials is None:
        return "No financial data available.\n"

    # financials dict mi dataclass mı?
    def fget(key):
        if isinstance(financials, dict):
            return financials.get(key)
        return getattr(financials, key, None)

    symbol = fget("symbol") or "N/A"

    fin_section = f"""
==============================
  FINANCIAL OVERVIEW — {symbol}
==============================

Revenue (TTM):        {fget("revenue_ttm")}
Quarterly Growth:     {fget("revenue_quarter")}
Net Income:           {fget("net_income")}
EPS (Trailing):       {fget("eps")}
P/E (Trailing):       {fget("pe")}
Forward P/E:          {fget("forward_pe")}
Price/Sales (TTM):    {fget("ps")}
PEG Ratio:            {fget("peg")}
Total Debt:           {fget("total_debt")}
Debt/Equity:          {fget("de_ratio")}
Free Cash Flow:       {fget("free_cash_flow")}
"""

    # -----------------------------
    # INSTITUTIONAL SECTION
    # -----------------------------
    inst_section = f"""
==============================
  INSTITUTIONAL HOLDERS — {symbol}
==============================
"""

    if institutional is None or not getattr(institutional, "top_holders", []):
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
