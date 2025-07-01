import asyncio
import time

from httpx import AsyncClient, Response


async def test_our_service(client_n: int) -> tuple[int, Response]:
    async with AsyncClient(timeout=9999) as client:
        return client_n, await client.get("http://localhost:8000/cpu")

async def main():
    n_clients = 10

    start_time = time.time()

    tasks = [asyncio.create_task(test_our_service(_)) for _ in range(n_clients)]

    print(f"[+] {n_clients} клиентов сейчас обращаются в наш сервис")

    for task in asyncio.as_completed(tasks):
        client, response = await task

        print(f"Клиента {client} обработал контейнер: {response.json()['hostname']}")

    elapsed_time = time.time() - start_time

    print(f"[+] Наш сервис обработал {n_clients} клиентов за {elapsed_time}")


if __name__ == "__main__":
    asyncio.run(main())
