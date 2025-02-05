import asyncio
async def main(username):
    print('Hello')
    await asyncio.sleep(1)
    print(f"... {username}!")


asyncio.run(main('Mayank Sanket'))
