import random
import asyncio
import math
import time
async def print_sorted(num):
    await asyncio.sleep((math.pi/2-math.atan(-num))/1000000)
    print(num)

async def main():
    test=[]
    for i in range(50):
        test.append(random.random()*random.randrange(0,101,10))
    for i in range(50):
        test.append(random.random()/random.randrange(1,102,10))
    for i in range(100):
        test.append(-(random.random()*random.randrange(0,101,10)))

    tasks = []
    for num in test:
        tasks.append(print_sorted(num))
    start=time.time()
    await asyncio.gather(*tasks)
    print(time.time()-start)

asyncio.run(main())
