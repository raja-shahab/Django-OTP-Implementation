import pyotp
from datetime import datetime, timedelta

def send_otp(request):
    toptp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = toptp.now()
    request.session['otp_secret_key'] = toptp.secret

    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)

    print(f"Your One Time Password is {otp}")
