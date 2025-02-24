import os
import pandas as pd

hashes_zweit = []
hashes_erst = []

def unique(current: list, file) -> bool:
    if hash(file) not in current:
        return True

for file in os.listdir("/Users/paulgies/Downloads/data"):
    if "erst" in file:
        f = open(f'/Users/paulgies/Downloads/data/{file}', "r").read()
        if unique(hashes_erst, f):
            hashes_erst.append(hash(f))
            with open(f'out/erst/{file}', "w") as fw:
                fw.write(f)
    if "zweit" in file:
        f = open(f'/Users/paulgies/Downloads/data/{file}', "r").read()
        if unique(hashes_zweit, f):
            hashes_zweit.append(hash(f))
            with open(f'out/zweit/{file}', "w") as fw:
                fw.write(f)

def create_df(path: str, df: pd.DataFrame) -> pd.DataFrame:
    with open(path, "r") as f:
        frame = pd.read_json(f)
    frame["date"] = path[-21:-11]
    df = pd.concat([df, frame])
    return df

erst = pd.DataFrame()
for file in os.listdir("/Users/paulgies/PycharmProjects/zweitstimme/out/erst/"):
    erst = create_df(f'/Users/paulgies/PycharmProjects/zweitstimme/out/erst/{file}', erst)

zweit = pd.DataFrame()
for file in os.listdir("/Users/paulgies/PycharmProjects/zweitstimme/out/zweit/"):
    zweit = create_df(f'/Users/paulgies/PycharmProjects/zweitstimme/out/zweit/{file}', zweit)

for file, name in zip([erst, zweit], ["erst.csv", "zweit.csv"]):
    file.to_csv(f'/Users/paulgies/PycharmProjects/zweitstimme/out/{name}')