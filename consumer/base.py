import abc
import asyncio

class BaseConsumer(abc.ABC):
    """Abstract base class for all consumers. Implements core consumption flow."""
    
    def __init__(self, auto_decode: bool = True):
        self.auto_decode = auto_decode
        self._running = False
        
    async def start(self):
        """Initialize consumer connections."""
        self._running = True
        
    async def stop(self):
        """Gracefully shutdown consumer."""
        self._running = False
        
    @abc.abstractmethod
    async def _receive(self):
        """Implement low-level message retrieval."""
        
    async def receive(self):
        """Get next message with optional decoding."""
        msg = await self._receive()
        return self.decode(msg) if self.auto_decode else msg
        
    def decode(self, data: bytes):
        """Convert raw bytes to usable format. Override for custom decoding."""
        try:
            return data.decode('utf-8')
        except UnicodeDecodeError:
            return data
