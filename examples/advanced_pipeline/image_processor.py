from fogverse.consumer import KafkaConsumer
from fogverse.producer import KafkaProducer
from fogverse.parallel import ParallelTask

class ImageProcessor(ParallelTask):
    """Processes images using parallel execution."""
    
    async def process(self, image_data: bytes) -> bytes:
        # Example: Apply image transformation
        return await self._apply_filter(image_data)

    async def _apply_filter(self, image_data: bytes) -> bytes:
        # Placeholder for actual image processing
        return image_data

async def main():
    consumer = KafkaConsumer(topics=['raw-images'])
    producer = KafkaProducer(topic='processed-images')
    
    async with ParallelContext(max_workers=4) as context:
        processor = ImageProcessor()
        async for message in consumer:
            processed = await context.process(processor.process, message.value)
            await producer.send(processed)
