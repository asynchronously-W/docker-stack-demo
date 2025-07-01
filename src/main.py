import time
from time import sleep

from fastapi import FastAPI
import socket

app = FastAPI(
    title="Docker Stack Demo"
)


@app.get("/hostname")
async def get_hostname() -> dict[str, str]:
    return {
        "hostname": socket.gethostname()
    }


@app.get("/cpu")
async def cpu_bound_task() -> dict[str, str]:
    start = time.time()

    sleep(3)

    elapsed_time = time.time() - start

    return {
        "elapsed_time": f"{elapsed_time}",
        "hostname": socket.gethostname()
    }
