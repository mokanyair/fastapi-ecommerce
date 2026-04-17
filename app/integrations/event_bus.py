import logging
from typing import Dict

logger = logging.getLogger(__name__)


def publish_event(event_type: str, payload: Dict) -> None:
    logger.info(f"EVENT: {event_type} → {payload}")