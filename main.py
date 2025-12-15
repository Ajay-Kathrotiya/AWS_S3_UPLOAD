from scripts.transform import transform_data
from scripts.upload_to_s3 import upload_file_to_s3
from scripts.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = "input_data/sales.csv"
OUTPUT_FILE = "processed_data/sales_cleaned.csv"

BUCKET_NAME = "ajay-de-project-demo-bucket"
S3_KEY = "processed/sales_cleaned.csv"

if __name__ == "__main__":
    try:
        logger.info("Application started")

        transform_data(INPUT_FILE, OUTPUT_FILE)
        upload_file_to_s3(OUTPUT_FILE, BUCKET_NAME, S3_KEY)

        logger.info("Application finished successfully")

    except Exception:
        logger.critical("Application failed", exc_info=True)
