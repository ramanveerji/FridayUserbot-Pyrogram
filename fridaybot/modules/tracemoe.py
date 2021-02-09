import tracemoepy
from fridaybot.function import progress, humanbytes, time_formatter, convert_to_image
from fridaybot.function.FastTelethon import upload_file

@friday.on(friday_on_cmd(pattern="tracemoe$"))
async def anime_name(event):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    file_s = await convert_to_image(event, friday)
    try:
      ws = tracemoe.search(file_s, encode=True)
    except:
      await event.edit("`SomeThing is Sad, Failed.`")
      return
    video = tracemoe.natural_preview(ws)
    with open('preview@FridayOT.mp4', 'wb') as f:
      f.write(video)
    starkfile = 'preview@FridayOT.mp4'
    warner = await upload_file(
            file_name=f"{ws.docs[0].title}.mp4",
            client=borg,
            file=open(starkfile, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Preview!", starkfile
                )
            ),
        )
    await friday.send_file(event.chat_id,
      warner,
      caption=str(ws.docs[0].title)
      )
