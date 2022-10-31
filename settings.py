import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = "vk1.a.3bBfOoRBHIEbKrY7Oa9-O_orT7AhKwh--_IvnmOSMa-_sGuWHZpCaIYQJQ1w2q5dJimgulWgQbNZZTzT_1kW5Qrtgp-9jeDFuhheexA3044DYTRwhkriAs1_iiqeutXKFFZb1U2U_q8qzSYmOM3u-Hj4COcRWcpN8X6RuHTQNomNOipMWg79Sh2IPUnH38VkWjiU8fDDsGGjeAc-fTdydQ"

group_id = 216899009

session = requests.Session()

vk_session = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk_session, group_id)

vk = vk_session.get_api()
