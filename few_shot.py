import json
import pandas as pd

class FewShotPosts:
    def __init__(self, file_path="data/processed_data.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        df = pd.json_normalize(posts)
        df['length'] = df['line_count'].apply(self.get_length)
        unique_tags=df['tags'].apply(lambda x:x).sum()
        self.df = df
        self.unique_tags = set(unique_tags)

    def get_length(self,line_count):
        if line_count<5:
            return "short"
        elif line_count<15:
            return "medium"
        else:
            return "long"
    def get_filtered_posts(self,length,language,tag):
        filtered_df=self.df[(self.df['length']==length) & (self.df['language']==language) & (self.df['tags'].apply(lambda x: tag in x))]
        return filtered_df        
if __name__ == "__main__":
    fs = FewShotPosts()
    print(fs.df)
