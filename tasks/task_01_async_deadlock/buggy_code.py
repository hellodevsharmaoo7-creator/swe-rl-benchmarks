import asyncio
import logging

class AsyncQueueWorker:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.lock = asyncio.Lock()
        self.processed_count = 0

    async def produce(self, item):
        await self.queue.put(item)

    async def consume(self):
        while not self.queue.empty():
            # BUG: Unhandled lock release on parsing failure causing deadlocks
            await self.lock.acquire()
            item = await self.queue.get()
            if item == "CORRUPTED":
                raise ValueError("Corrupted payload")
            self.processed_count += 1
            self.lock.release()
