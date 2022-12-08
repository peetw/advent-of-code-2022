import pandas as pd

BASE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

ROUND_SCORE = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

CHOICE = {
    'AX': 'Z',
    'AY': 'X',
    'AZ': 'Y',
    'BX': 'X',
    'BY': 'Y',
    'BZ': 'Z',
    'CX': 'Y',
    'CY': 'Z',
    'CZ': 'X'
}


def part_1(file_path: str):
    df = pd.read_csv(file_path, sep=' ', header=None, names=['them', 'us'])
    df_count = df.groupby(['them', 'us']).size().reset_index(name='count')
    return calc_total_score(df_count)


def part_2(file_path: str):
    df = pd.read_csv(file_path, sep=' ', header=None, names=['them', 'result'])
    df_count = df.groupby(['them', 'result']).size().reset_index(name='count')
    df_count['us'] = df_count.apply(lambda row: CHOICE[row['them'] + row['result']], axis=1)
    return calc_total_score(df_count)


def calc_total_score(df: pd.DataFrame) -> int:
    df['score'] = df.apply(calc_score, axis=1)
    total_score = sum(df['count'] * df['score'])
    return total_score


def calc_score(row: pd.Series) -> int:
    base_score = BASE_SCORE[row['us']]
    round_score = ROUND_SCORE[row['them'] + row['us']]
    score = base_score + round_score
    return score
