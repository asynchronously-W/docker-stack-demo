import asyncio
import time

from httpx import AsyncClient, Response


async def test_our_service() -> Response:
    async with AsyncClient(timeout=9999) as client:
        return await client.get("http://localhost:8000/cpu")

async def main():
    n_clients = 10

    start_time = time.time()

    tasks = [asyncio.create_task(test_our_service()) for _ in range(n_clients)]

    print(f"[+] {n_clients} клиентов сейчас обращаются в наш сервис")

    results = await asyncio.gather(*tasks)

    print(results)

    elapsed_time = time.time() - start_time

    print(f"[+] Наш сервис обработал {n_clients} клиентов за {elapsed_time}")


if __name__ == "__main__":
    asyncio.run(main())
