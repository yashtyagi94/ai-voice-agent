import pandas as pd
import os

def log_metrics(eou, ttft, ttfb, total_latency, session_id):
    file_path = 'metrics.xlsx'
    data = {
        'Session ID': [session_id],
        'EOU (s)': [eou],
        'TTFT (s)': [ttft],
        'TTFB (s)': [ttfb],
        'Total Latency (s)': [total_latency]
    }

    df = pd.DataFrame(data)

    if not os.path.exists(file_path):
        # File doesn't exist; create it with headers
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False, sheet_name='Metrics')
    else:
        # File exists; append without headers
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            existing_df = pd.read_excel(file_path, sheet_name='Metrics')
            start_row = len(existing_df) + 1
            df.to_excel(writer, index=False, header=False, sheet_name='Metrics', startrow=start_row)
