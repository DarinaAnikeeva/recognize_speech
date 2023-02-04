import json
import environs
import argparse
import logging

import google.api_core.exceptions
import google.cloud.dialogflow_v2 as dialogflow
import requests

logger = logging.getLogger(__name__)

def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent})


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--json',
        type=str,
        help='Локальный путь до файла'
    )
    parser.add_argument(
        '--url',
        type=str,
        help="Ссылка до json файла"
    )
    args = parser.parse_args()

    env = environs.Env()
    env.read_env()
    project_id = env.str('PROJECT_ID')

    try:
        if args.url:
            url = args.url
            response = requests.get(url)
            response.raise_for_status()
            intents = response.json()
        elif args.json:
            with open(args.json, 'r') as file:
                params = file.read()
            intents = json.loads(params)

        for display_name in intents:
            answer = intents[display_name]['answer']
            questions = intents[display_name]['questions']
            create_intent(
                project_id=project_id,
                display_name=display_name,
                training_phrases_parts=questions,
                message_texts=answer)

        print('Complete!')
    except requests.exceptions.HTTPError as err:
        logger.error(err)
        pass
    except requests.exceptions.ConnectionError as err:
        logger.error(err)
        pass
    except json.decoder.JSONDecodeError as err:
        logger.error(err)
        pass
