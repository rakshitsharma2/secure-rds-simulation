import secrets

new_password = secrets.token_urlsafe(16)

print("New Password:", new_password)