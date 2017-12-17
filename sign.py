import hmac, hashlib

DateKey = hmac.new(b'AWS4<YOUR_SECRET_KEY>', b'20171217', hashlib.sha256).digest()

DateRegionKey = hmac.new(DateKey, b'us-east-1', hashlib.sha256).digest()

DateRegionServiceKey = hmac.new(DateRegionKey, b's3', hashlib.sha256).digest()

SigningKey = hmac.new(DateRegionServiceKey, b'aws4_request', hashlib.sha256).digest()

string_to_sign = '''<YOUR_BASE64_ENCODED_POLICY>'''

signature = hmac.new(SigningKey, string_to_sign, hashlib.sha256).hexdigest()
print('policy signature: ' + signature)

