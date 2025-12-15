import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from scripts.logger import get_logger

logger = get_logger(__name__)

def upload_file_to_s3(file_path, bucket_name, s3_key):
    try:
        logger.info(f"Uploading {file_path} to s3://{bucket_name}/{s3_key}")

        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, s3_key)

        logger.info("File uploaded to S3 successfully")

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}", exc_info=True)
        raise

    except NoCredentialsError:
        logger.error("AWS credentials not found", exc_info=True)
        raise

    except ClientError as e:
        logger.error("AWS Client error occurred", exc_info=True)
        raise

    except Exception:
        logger.error("Unexpected error during S3 upload", exc_info=True)
        raise