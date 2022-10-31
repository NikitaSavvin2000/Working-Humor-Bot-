from settings import *
from data import *


def send_photo():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            message = event.object['message']['text']
            upload = vk_api.VkUpload(vk)
            photo_DA = upload.photo_messages('photo\\Yes.png')
            photo_NET = upload.photo_messages('photo\\No.png')
            photo_OK = upload.photo_messages('photo\\Ok.png')
            if message in DA:
                owner_id = photo_DA[0]['owner_id']
                photo_id = photo_DA[0]['id']
                access_key = photo_DA[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                vk.messages.send(chat_id=event.chat_id, random_id=0, attachment=attachment)
            elif message in NET:
                owner_id = photo_NET[0]['owner_id']
                photo_id = photo_NET[0]['id']
                access_key = photo_NET[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                vk.messages.send(chat_id=event.chat_id, random_id=0, attachment=attachment)
            elif message in OK:
                owner_id = photo_OK[0]['owner_id']
                photo_id = photo_OK[0]['id']
                access_key = photo_OK[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                vk.messages.send(chat_id=event.chat_id, random_id=0, attachment=attachment)
