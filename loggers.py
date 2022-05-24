import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def warning_logger():
    logger.warning("This is warning")

def info_logger():
    logger.info("This is information")

def main():
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    stream_hander = logging.StreamHandler()  # 이게 모지 -> 아하 실행하면 콘솔창에 쭉 띄워주는 거구나
    mylogger.addHandler(stream_hander)

    mylogger.info("server start!!!")


if __name__ == "__main__":
    main()
