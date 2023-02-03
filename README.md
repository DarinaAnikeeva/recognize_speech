# Распознание речи от пользователя
В коде есть 2 бота: один для `ВКонтакте`, второй для `Телеграма`.

С их помощью, если пользователь задаст вопрос, на который есть стандартный ответ, то бот ответит сам, через неиросеть

Вопросы и ответы также можно добавлять, об этом будет сказано ниже

## Для запуска
Скачайте код:
```sh
git clone https://github.com/devmanorg/star-burger.git
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` придётся использовать `python3` или `py -3`

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```

Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

## Определите переменные окружения.
1. Создать файл `.env` в каталоге и положите туда следующие переменные окружения:
    * TG_BOT_TOKEN - необходимо создать телеграмм-бота, https://telegram.me/BotFather напишите команду /newbot. В результате создания бота, вам будет прислан примерно такой токен:
```958423683:AAEAtJ5Lde5YYfu8GldVhSG```
    * PROJECT_ID - [перейдите по ссылке](https://dialogflow.cloud.google.com/#/getStarted) и нажмите на кнопку [create agent](https://cloud.google.com/dialogflow/es/docs/quick/build-agent). После создания проекта вас будет дан PROJECT ID, его и нужно сюда вставить
    * GOOGLE_APPLICATION_CREDENTIALS - положите сюда:
```C:\Users\ultra\AppData\Roaming\gcloud\application_default_credentials.json```
. Загрузите [установщик Google Cloud CLI](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe), следуйте подсказкам. После установки пишем в командной строке gcloud auth application-default login (создаст джейсон для авторизации по умолчанию, будет находиться)
    * VK_TOKEN - [создайте сообщество ВКонтакте](https://vk.com/groups?tab=admin). Токен нужно создать в настройках сообщества в меню Работа с API
