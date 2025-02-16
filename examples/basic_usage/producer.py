from fogverse.producer.kafka import KafkaProducer
from fogverse.utils.logging import FogLogger

class MyProducer(KafkaProducer):
    def __init__(self):
        super().__init__(
            topic="my-topic",
            bootstrap_servers="localhost:9092"
        )
        self.logger = FogLogger("MyProducer")
        
    async def produce(self, data: str):
        await self.send(data.encode())
        self.logger.info(f"Sent: {data}")

async def main():
    producer = MyProducer()
    await producer.start()
    for i in range(10):
        await producer.produce(f"Message {i}")
    await producer.stop()

if __name__ == "__main__":
    asyncio.run(main())
