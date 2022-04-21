class Config:
    host = 'localhost'
    queue = 'garage-remote'
    routing_key = 'garage.remote.channel'
    topic_exchange_name = 'garage-remote-exchange'

    RESPONSE_KEY = "RASPI"
