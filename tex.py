from twitter import tweep
import pandas as pd

def cs(keyword):
    df = pd.DataFrame(tweep(keyword))
    df.to_csv("tweets.csv", index=False, header=False)

if __name__ == "__main__":
    cs(input("Enter: "))
    