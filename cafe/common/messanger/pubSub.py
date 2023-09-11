import os
import logging
from google.cloud import pubsub_v1
import google.auth


async def init() -> pubsub_v1.PublisherClient:
    credentials, project = google.auth.default()
    publisher = pubsub_v1.PublisherClient()

    return publisher

async def create_topic(publisher: pubsub_v1.PublisherClient, topic_name: str) -> None:
    topic_path = publisher.topic_path(os.environ.get("PROJECT_ID"), topic_name)

    try:
        publisher.get_topic(request={"topic": topic_path})
        publisher.create_topic(request={"name": topic_path})

    except Exception as e:
        logging.error(f"Error when creating topic: {topic_name}")
     

async def pub_message(publisher: pubsub_v1.PublisherClient, topic_name: str, message: str) -> None:
    try:
        future = publisher.publish(topic_name, message.encode('utf-8'))
        logging.debug(future.result())

    except Exception as e:
        logging.error(f"Error when publishing message: {message} to topic: {topic_name}")

async def consume_message() -> None:
    pass