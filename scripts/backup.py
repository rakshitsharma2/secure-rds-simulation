import os

os.system(
    "docker exec secure_mysql "
    "mysqldump -uroot -prootpass123 securedb "
    "> backup.sql"
)

print("Backup Complete")