from werkzeug.security import generate_password_hash, check_password_hash

hashed_pwd1 = generate_password_hash("password", method="MD5", salt_length=8)
print(f"The password string is 'password'.\nhashed_pwd1 is {hashed_pwd1}")
check1 = check_password_hash(hashed_pwd1, "password")
print(f"check is {check1}\n")

hashed_pwd2 = generate_password_hash("password")
print(f"The password string is 'password'.\nhashed_pwd2 is {hashed_pwd2}")
check2 = check_password_hash(hashed_pwd2, "password")
print(f"check is {check2}\n")

hashed_pwd3 = generate_password_hash("password", method="pbkdf2:sha512:1000", salt_length=16)
print(f"The password string is 'password'.\nhashed_pwd3 is {hashed_pwd3}")
check3 = check_password_hash(hashed_pwd3, "password")
print(f"check is {check3}\n")