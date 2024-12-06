import os
from dhooks import Webhook, Embed, File

image2_path = 'boruto.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[BORUTO link - click here -](https://sip.elfak.ni.ac.rs/)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://boruto.png")
    file = File(image2_path, name="boruto.png")
    hook.send("@everyone 📢 BORUTO", embed=embed, file=file)
