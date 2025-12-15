import pandas as pd
from scripts.logger import get_logger

logger = get_logger(__name__)

def transform_data(input_file, output_file):
    try:
        logger.info(f"Reading input file: {input_file}")

        df = pd.read_csv(input_file)

        logger.info("Handling missing values")
        df['price'] = df['price'].fillna(0)

        logger.info("Creating total_amount column")
        df['total_amount'] = df['price'] * df['quantity']

        df.to_csv(output_file, index=False)

        logger.info(f"Data transformation successful. Output saved to {output_file}")

    except FileNotFoundError:
        logger.error(f"Input file not found: {input_file}", exc_info=True)
        raise

    except Exception as e:
        logger.error("Unexpected error during data transformation", exc_info=True)
        raise