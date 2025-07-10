import logging
from lesson_21.utils import time_extractor


def hb_detector(timestamps):
    logging.basicConfig(
        filename='hb_test.txt',
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True)
    logger = logging.getLogger("hb_detector")
    for i in range(len(timestamps) - 1):
        delta = (timestamps[i] - timestamps[i + 1]).total_seconds()
        if 31 < delta < 33:
            logger.warning(f"Heartbeat більше 31 сек але менше 33 і складає: {delta} секунд."
                           f" Час виникнення помилки: {timestamps[i].strftime('%H:%M:%S')}.")
        elif delta >= 33:
            logger.error(f"Heartbeat більше 33 і складає: {delta} секунд."
                         f" Час виникнення помилки: {timestamps[i].strftime('%H:%M:%S')}.")


if __name__ == '__main__':
    hb_detector(time_extractor())
