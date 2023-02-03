import vk_api
import environs
import random
from dialogflow_function import detect_intent_texts
from vk_api.longpoll import VkLongPoll, VkEventType



def send_message(user_id, text):
    vk_api.messages.send(
        user_id=user_id,
        message=text,
        random_id=random.randint(1, 1000)
    )

def receive_message(session_id, project_id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer = detect_intent_texts(
                project_id=project_id,
                session_id=session_id,
                text=event.text,
                language_code='ru')

            if answer:
                send_message(event.user_id, answer)


if __name__ == "__main__":
    env = environs.Env()
    env.read_env()

    project_id = env.str('PROJECT_ID')
    vk_token = env.str('VK_TOKEN')

    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    receive_message(vk_session, project_id)