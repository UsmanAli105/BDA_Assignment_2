import pandas as pd
import os, glob

if __name__ == '__main__':
    root_dir = 'data/youtube_data'
    json_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    for i in range(len(json_files)):
        df = pd.read_json(json_files[i], lines=True)
        print(df.iloc[0][''])