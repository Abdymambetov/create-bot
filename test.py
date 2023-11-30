# from decouple import config
# from time import sleep
from asyncio import sleep, gather, run, create_task
# name = config("NAME", default='Python')
# print(name)
# print(type(name))


# pwd = config("PASSWORD", default='123456', cast=int)
# print(pwd, type(pwd))

def name(fulname: str) -> list:
    return fulname.split("-")

print(name("abdymambetov-meder"))

i=2
x=[]
while i<=6:
    x.append(i)
    i=i+2

print(x)

# async def download_photo(photo_count: int, limit: int):
#     while photo_count < limit:
#         await sleep(1)
#         photo_count+=1
#         print(f"Photo: {photo_count}...")

# async def download_video(video_count: int, limit: int):
#     while video_count < limit:
#         await sleep(5)
#         video_count+=1
#         print(f"Video: {video_count}...")

# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count, 10),
#         download_video(video_count, 3)
#     ]
#     await gather(*task_list)

# run(main())


#new
async def download_photo2(photo_count):
    await sleep(1)
    print(f"Photo2: {photo_count}")

async def main2():
    count = int(input("Enter amount: "))
    current_photo = 0
    task_list = []

    while current_photo < count:
        current_photo +=1
        # download_photo2(current_photo)
        task = create_task(download_photo2(current_photo))
        task_list.append(task)
    await gather(*task_list)

run(main2())



#
a =[1,2,3,4]
b = ['a', 'b', 'c']

a.append(b)
print(a)