from fogverse.consumer.kafka import KafkaConsumer
from fogverse.utils.logging import FogLogger

class MyConsumer(KafkaConsumer):
    def __init__(self):
        super().__init__(
            topics=["my-topic"],
            bootstrap_servers="localhost:9092"
        )
        self.logger = FogLogger("MyConsumer")
        
    async def process(self, message: str):
        self.logger.info(f"Received: {message}")

async def main():
    consumer = MyConsumer()
    await consumer.start()
    while True:
        message = await consumer.receive()
        await consumer.process(message)

if __name__ == "__main__":
    asyncio.run(main())
