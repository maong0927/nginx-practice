# nginx-practice
nginx 연습용 레포 

## 1. gunicorn - nginx 
### gunicorn
참고 
1. https://docs.gunicorn.org/en/stable/settings.html
2. https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

실행
`gunicorn -c gunicorn.conf.py run_webapp:app`
