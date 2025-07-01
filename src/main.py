import time

from fastapi import FastAPI
import socket

app = FastAPI(
    title="Docker Stack Demo"
)


@app.get("/hostname")
def get_hostname() -> dict[str, str]:
    return {
        "hostname": socket.gethostname()
    }


@app.get("/cpu")
def cpu_bound_task() -> dict[str, str]:
    start = time.time()

    cpu = [_ for _ in range(100_000_000)]

    elapsed_time = time.time() - start

    return {
        "elapsed_time": f"{elapsed_time}",
        "hostname": socket.gethostname()
    }
