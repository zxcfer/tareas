import uvicorn
import fastapi


@app.on_event("startup")
@repeat_every(seconds=10) 
def clean_queue() -> None:
    for msg in app.queue:
        print(msg)


if __name__ == "__main__":
    uvicorn.run(
        "server:app", 
        host="127.0.0.1", 
        port=65432,
        log_level="info")