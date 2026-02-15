import csv
import os
from datetime import datetime

LOG_FILE = "log.csv"

def init_log():
    """
    Create log.csv if it does not exist.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "symbol",
                "source",
                "status",
                "message",
                "output_type"
            ])

def write_log(symbol: str, source: str, status: str, message: str, output_type: str):
    """
    Append a new log entry.
    """
    init_log()

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            symbol,
            source,
            status,
            message,
            output_type
        ])
