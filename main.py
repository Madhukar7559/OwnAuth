import base64
import hashlib
import hmac
from typing import Any, Optional
import pyscript as ps
import calendar
import datetime
import hashlib
import time
from typing import Any, Optional, Union
import csv
import time

digest = hashlib.sha1

def sec(secret):
    missing_padding = len(secret) % 8
    if missing_padding != 0:
        secret += "=" * (8 - missing_padding)
    return base64.b32decode(secret, casefold=True)

@staticmethod
def int_to_bytestring(i: int, padding: int = 8) -> bytes:
    result = bytearray()
    while i != 0:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(bytearray(reversed(result)).rjust(padding, b"\0"))

def generate_otp(value, secret):
    hasher = hmac.new(sec(secret), int_to_bytestring(value), digest)
    hmac_hash = bytearray(hasher.digest())
    offset = hmac_hash[-1] & 0xF
    code = (
            (hmac_hash[offset] & 0x7F) << 24
            | (hmac_hash[offset + 1] & 0xFF) << 16
            | (hmac_hash[offset + 2] & 0xFF) << 8
            | (hmac_hash[offset + 3] & 0xFF)
        )
    str_code = str(10_000_000_000 + (code % 10**6))
    return str_code[-6 :]

def timecode(length: datetime.datetime):
    if length:
        return int(calendar.timegm(length.utctimetuple()) / 30)
    else:
        return int(time.mktime(length.timetuple()) /30)
def at(s) -> str:
    return generate_otp(timecode(datetime.datetime.fromtimestamp(int(time.time()) + 30)) - 660,s)

def now(s) -> str:
    return generate_otp(timecode(datetime.datetime.now()) - 660,s)

file_path = 'sec_keys.csv'

issuer_name_sec = []

with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        issuer_name_sec.append(row)

table_html = '<table border=0><thead><tr>'
table_html += ''.join(f'<th style:"padding: 100px;">{header}</th>' for header in issuer_name_sec[0]) + f'<th style:"padding: 100px;">NEXT</th>'
table_html += '</tr></thead><tbody>'
            
for row in issuer_name_sec[1:]:
    table_html += '<tr>'
    table_html += f'<td style:"padding: 100px;">{row[0]}</td>' + f'<td style:"padding: 100px;">{now(row[1])}</td>' + f'<td style:"padding: 100px;">{at(row[1])}</td>'
    table_html += '</tr>'
            
table_html += '</tbody></table>'

ps.document.getElementById("otp").innerHTML = table_html
