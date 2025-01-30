from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def receive_data(request: Request):
    # Получаем данные из запроса
    data = await request.json()
    print(data)  # Выводим данные в консоль для проверки
    return JSONResponse(content={"status": "success", "data_received": data})
