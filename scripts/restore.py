import os

os.system(
    "docker exec -i secure_mysql "
    "mysql -uroot -prootpass123 securedb "
    "< backup.sql"
)

print("Restore Complete")