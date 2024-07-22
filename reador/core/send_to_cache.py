import requests

from config import *

async def send_to_cache(msg, send_data):
    headers = {AUTH: AUTH_KEY}
    
    try:
        try:
            dest_url = URL+"/"+AUTH # does this if you have a site up
            response = requests.post(dest_url, json=send_data, headers=headers)
        
        except:
            dest_url = 'http://localhost:5000/'+AUTH
            response = requests.post(dest_url, json=send_data, headers=headers)
    
        if response.status_code == 200:
            await msg.channel.send("Data sent to memory successfully.")
        else:
            await msg.channel.send("Failed to send data to memory.")

    except requests.RequestException as e:
        await msg.channel.send(f"Error occurred while sending data: {e}")