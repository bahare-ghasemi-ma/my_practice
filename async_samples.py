# #--------Concurrent API Requests with asyncio--------
# import asyncio
# import time

# async def fetch_data(api_name, delay):
#     print(f"Fetching data from {api_name}...")
#     await asyncio.sleep(delay)  # Simulates network delay
#     print(f"Data fetched from {api_name} after {delay} seconds")
#     return f"Data from {api_name}"

# async def main():
#     start_time = time.time()

#     # Create two async tasks
#     task1 = asyncio.create_task(fetch_data('API 1', 2))
#     task2 = asyncio.create_task(fetch_data('API 2', 3))

#     # Await both tasks to complete
#     results = await asyncio.gather(task1, task2)

#     end_time = time.time()

#     print(f"Results: {results}")
#     print(f"Completed in {end_time - start_time:.2f} seconds")

# # Run the event loop
# asyncio.run(main())

# #---------Running Multiple Tasks with asyncio.gather()-------

# import asyncio

# async def task(id, delay):
#     print(f"Task {id} starting...")
#     await asyncio.sleep(delay)
#     print(f"Task {id} completed after {delay} seconds")
#     return f"Result of Task {id}"

# async def main():
#     tasks = [
#         asyncio.create_task(task(1, 2)),
#         asyncio.create_task(task(2, 3)),
#         asyncio.create_task(task(3, 1))
#     ]

#     # Await all tasks to complete and gather their results
#     results = await asyncio.gather(*tasks)
#     print(f"All tasks completed with results: {results}")

# # Run the event loop
# asyncio.run(main())
# #-----------Using asyncio.wait() for Timeouts----------
# import asyncio

# async def long_running_task():
#     print("Task started")
#     await asyncio.sleep(5)
#     print("Task finished")
#     return "Completed"

# async def main():
#     try:
#         # Run task with a 2-second timeout
#         result = await asyncio.wait_for(long_running_task(), timeout=2)
#         print(result)
#     except asyncio.TimeoutError:
#         print("Task timed out")

# # Run the event loop
# asyncio.run(main())
# #------------Running Tasks Sequentially with async/await--------
# import asyncio

# async def task(id, delay):
#     print(f"Task {id} starting...")
#     await asyncio.sleep(delay)
#     print(f"Task {id} completed after {delay} seconds")
#     return f"Result of Task {id}"

# async def main():
#     result1 = await task(1, 2)  # Runs first
#     result2 = await task(2, 1)  # Runs after result1 completes
#     result3 = await task(3, 3)  # Runs after result2 completes

#     print(f"Results: {result1}, {result2}, {result3}")

# # Run the event loop
# asyncio.run(main())
#--------Async Context Managers (async with)----------
# import asyncio
import random

# class AsyncResource:
#     async def __aenter__(self):
#         print("Acquiring resource")
#         await asyncio.sleep(1)
#         return self
#
#     async def __aexit__(self, exc_type, exc_value, traceback):
#         print("Releasing resource")
#         await asyncio.sleep(1)
#
#     async def process(self):
#         await asyncio.sleep(random.uniform(0.5, 1.5))
#         print("Processing resource")
#
# async def main():
#     async with AsyncResource() as resource:
#
#         await resource.process()

# Run the event loop
# asyncio.run(main())
# #----------------asyncio.as_completed() for Task Completion Order-----------
# import asyncio

# async def task(id, delay):
#     print(f"Task {id} starting...")
#     await asyncio.sleep(delay)
#     print(f"Task {id} completed after {delay} seconds")
#     return f"Result of Task {id}"

# async def main():
#     tasks = [
#         task(1, 3),
#         task(2, 1),
#         task(3, 2)
#     ]

#     for result in asyncio.as_completed(tasks):
#         res = await result
#         print(res)

# # Run the event loop
# asyncio.run(main())
# #---------------------------------

import asyncio
from random import randint

async def get_weather_city(city:str):
    print(f"getting weather for {city}")

    await asyncio.sleep(randint(5,10))

    return city , randint(9,30)



def main ():

    city=["mashhad","tehran","tabriz","bandarabas"]

    for i in city:
        tasks = [asyncio.create_task(i)]

asyncio.run(main())