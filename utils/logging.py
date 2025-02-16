import logging
import sys

class FogLogger:
    """Unified logging handler with configurable outputs."""
    
    def __init__(self, name: str, level=logging.INFO, log_file: str = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        
        # File handler
        if log_file:
            file = logging.FileHandler(log_file)
            file.setFormatter(formatter)
            self.logger.addHandler(file)
            
    def log(self, level: str, message: str, **kwargs):
        """Generic log method with structured context support."""
        getattr(self.logger, level.lower())(message, extra=kwargs)
