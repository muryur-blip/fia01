from assets import ASSETS
from pipelines.financials import get_financials
from pipelines.institutional import get_institutional_holders
from output.formatter import format_report
from logging_utils import write_log

def run_fia01():
    print("\n=== FIA-01 Weekly Analyst Starting ===\n")

    for symbol in ASSETS:
        print(f"Processing {symbol}...")

        # --- Financials ---
        fin = get_financials(symbol)
        if "error" in fin:
            write_log(symbol, "financials", "fail", fin["error"], "none")
        else:
            write_log(symbol, "financials", "success", "ok", "dict")

        # --- Institutional ---
        inst = get_institutional_holders(symbol)
        if "error" in inst:
            write_log(symbol, "institutional", "fail", inst["error"], "none")
        else:
            write_log(symbol, "institutional", "success", "ok", "list")

        # --- Format Report ---
        report = format_report(fin, inst)

        # Print to console for now
        print(report)
        print("\n--------------------------------------\n")

    print("=== FIA-01 Completed ===")

if __name__ == "__main__":
    run_fia01()
