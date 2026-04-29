import asyncio

async def download(name):
    print(f"Downloading {name}...")
    await asyncio.sleep(2)

async def main():
    tasks = [
        download("dataset1"),
        download("dataset2"),
        download("dataset3")
    ]
    await asyncio.gather(*tasks)
    print("All downloads complete.")

asyncio.run(main())