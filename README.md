# Telebot Service
A service that serves the messages that the messaging service enqueues, and also acts as a simple Flask application that the Telegram API webhooks to so that users can register themselves.

### Setup
Exactly the same as the messaging service. Just follow that. To connect to the db, just run `heroku psql`.

### Limitations
If the service is idling, it needs to be manually restarted by making a any kind of request to https://itsa-telebot-service.herokuapp.com/
