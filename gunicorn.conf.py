# 1. gunicorn을 시작할 때마다 실행
import multiprocessing

bind = "0.0.0.0:7777"
wsgi_app="run_webapp:app"
# The number of worker processes. This number should generally be between 2-4 workers per core in the server.
workers = multiprocessing.cpu_count() * 2 + 1