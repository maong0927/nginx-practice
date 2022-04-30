from app import create_app

# 진입점 생성
app = create_app()
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=7777,
        debug=True,
        use_reloader=False,
    )
