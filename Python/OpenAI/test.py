

[Unit]
Description=Ruby App

[Service]
Environment="SECRET_KEY_BASE=<любая строка>"
Environment="RAILS_ENV=production"
Environment="RAILS_LOG_TO_STDOUT=1"
Environment="DB_HOST=127.0.0.1"
Environment="DB_PORT=5432"
Environment="DB_NAME=<имя базы данных>"
Environment="DB_USER=<пользователь в базе данных>"
Environment="DB_PASSWORD=<пароль для базы данных>"
ExecStart=<путь до исполняемого файла>

[Install]
WantedBy=multi-user.target