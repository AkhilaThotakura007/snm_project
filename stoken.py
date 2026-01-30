from itsdangerous import URLSafeSerializer
secret_key='akhila'
salt='Otpverify'
def endata(data):
    serializer=URLSafeSerializer(secret_key)
    return serializer.dumps(data,salt=salt)
def dndata(data):
    serializer=URLSafeSerializer(secret_key)
    return serializer.loads(data,salt=salt)
