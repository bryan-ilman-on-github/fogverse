from confluent_kafka.admin import AdminClient, NewTopic

async def create_topics(config: dict):
    """Create Kafka topics with specified configurations."""
    admin = AdminClient({'bootstrap.servers': config['bootstrap_servers']})
    topics = [
        NewTopic(
            name=topic['name'],
            num_partitions=topic.get('partitions', 1),
            replication_factor=topic.get('replication_factor', 1),
            config=topic.get('config', {})
        )
        for topic in config.get('topics', [])
    ]
    futures = admin.create_topics(topics)
    for topic, future in futures.items():
        try:
            future.result()
            print(f"Created topic: {topic}")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")
