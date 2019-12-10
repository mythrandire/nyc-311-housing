import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", "PXkXxMVDwDUe5OaptO5qTbo2e",
                 username="dso2119@columbia.edu", password="Providence@024")


client.timeout = 500
results = client.get("erm2-nwe9", limit=500000)
raw_311_df = pd.DataFrame.from_records(results)
zip_311_df = raw_311_df.filter(items=['created_date', 'complaint_type', 'incident_zip', 'status'])
no_nan_df = zip_311_df.dropna()
no_nan_df.reset_index(drop=True, inplace=True)
no_nan_df.head(500000)
