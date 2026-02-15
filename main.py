import os
from pipelines.financials import get_financials
from pipelines.institutional import get_institutional_holders
from output.formatter import format_report
from logging_utils import write_log, init_log
from assets import ASSETS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# -----------------------------
# EMAIL SENDER
# -----------------------------
def send_email(report_text: str):
    sender = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL")  # kendine gönderiyorsun

    if not sender or not password:
        print("Email credentials missing — EMAIL or EMAIL_PASSWORD not found.")
        return

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "FIA-01 Weekly Report"
    msg.attach(MIMEText(report_text, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Email sending failed:", e)


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    print("FIA-01 started.")
    init_log()

    full_report = ""

    for asset in ASSETS:
        print(f"Processing {asset}...")

        try:
            financials = get_financials(asset)
            institutional = get_institutional_holders(asset)

            report = format_report(financials, institutional)
            full_report += report + "\n\n"

            write_log(
                symbol=asset,
                source="FIA-01",
                status="success",
                message="Processed successfully",
                output_type="text"
            )

        except Exception as e:
            write_log(
                symbol=asset,
                source="FIA-01",
                status="error",
                message=str(e),
                output_type="text"
            )
            print(f"Error processing {asset}: {e}")

    # Email final combined report
    send_email(full_report)

    print("FIA-01 completed.")


if __name__ == "__main__":
    main()
