#!/usr/bin/env python3
"""Send an email via Gmail SMTP using credentials in .env.

CLI:        _email.py "<subject>" "<body>"   -> prints "sent" / "FAILED: <reason>"
Importable: send(subject, body) -> (ok: bool, detail: str)

Reads from .env: SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_APP_PASSWORD, ALERT_EMAIL_TO.
Port 465 -> implicit SSL; 587 -> STARTTLS. Never raises to the caller (returns the
failure as a string) so a hook can't crash the session on a transient mail error.
"""
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage

_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env")


def _load_env():
    d = {}
    try:
        with open(_ENV) as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    d[k.strip()] = v.strip()
    except FileNotFoundError:
        pass
    return d


def send(subject, body):
    e = _load_env()
    host = e.get("SMTP_HOST", "smtp.gmail.com")
    try:
        port = int(e.get("SMTP_PORT", "465"))
    except ValueError:
        port = 465
    user = e.get("SMTP_USER")
    pw = e.get("SMTP_APP_PASSWORD")
    to = e.get("ALERT_EMAIL_TO", user)
    if not (user and pw and to):
        return False, "missing SMTP_USER / SMTP_APP_PASSWORD / ALERT_EMAIL_TO in .env"
    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    ctx = ssl.create_default_context()
    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, context=ctx, timeout=20) as s:
                s.login(user, pw)
                s.send_message(msg)
        else:
            with smtplib.SMTP(host, port, timeout=20) as s:
                s.ehlo()
                s.starttls(context=ctx)
                s.login(user, pw)
                s.send_message(msg)
        return True, "sent to %s" % to
    except Exception as ex:
        return False, "%s: %s" % (type(ex).__name__, ex)


if __name__ == "__main__":
    subj = sys.argv[1] if len(sys.argv) > 1 else "origin-node test"
    body = sys.argv[2] if len(sys.argv) > 2 else "test body"
    ok, detail = send(subj, body)
    print("sent" if ok else "FAILED: " + detail)
    sys.exit(0 if ok else 1)
