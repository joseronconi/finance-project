import fundamentus
import pandas as pd
import nasdaqdatalink
import investpy as inv
import lib_aws as aws

def main():

    # Create Function to save as parquet
    def save_upload_parquet(session, bucket, df, filename):

        pd.DataFrame(df).to_parquet(filename)
        aws.upload_to_aws(session, bucket, filename)

    # create session to s3   
    session = aws.create_session()
    bucket = 'project-finance-api'

    # Get KPIs from fundamentus
    save_upload_parquet(session, bucket, fundamentus.get_resultado(), "fundamentus.parquet")

    # Get CDI from Nasdaq
    save_upload_parquet(session, bucket, nasdaqdatalink.get("BCB/4391", authtoken="tixYdHPLhTfCwsD8zW2p"), "nasdaq.parquet")

    # Get list of tickets
    save_upload_parquet(session, bucket, inv.get_stocks(country='brazil'), "investpy.parquet")


if __name__ == '__main__':
    main() 