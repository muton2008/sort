import asyncio
import math

class SleepSort:
    def __init__(self, data: list):
        self.data = data
        self.done=[]
        
    async def sort(self, num):
        await asyncio.sleep((math.pi/2 - math.atan(-num))/1000000)
        self.done.append(num)

    async def prepare(self):
        self.tasks = []
        for num in self.data:
            self.tasks.append(self.sort(num))
    def main(self):
        asyncio.run(self.prepare())
        asyncio.run(asyncio.gather(*self.tasks))
        return self.done
