import os
from dhooks import Webhook, Embed, File

image2_path = 'boruto.jpeg'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[BORUTO link - click here -](https://www.animesrbija.com/anime/boruto-naruto-next-generations)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://boruto.jpeg")
    file = File(image2_path, name="boruto.jpeg")
    hook.send("@everyone 📢 BORUTO", embed=embed, file=file)
