from thefuzz import fuzz
from thefuzz import process


def fuzzy(df, column, min_index=80, max_index=100):
    """Simple ratio function for string matching using fuzzy search. Good for single strings.

    Args:
        df (_pd.DataFrame_): pandas dataframe containing the corresponding column.
        column (_str_): the column to be searched; string.
        min_index (int, optional): min fuzzy index to match. Defaults to 80.
        max_index (int, optional): min fuzzy index to match. Defaults to 100.
    """
    col_name = str(column)
    id = []
    idx = 0

    for i in df[column][1:]:
        col0 = df[column][idx]
        col1 = i
        match_id = fuzz.ratio(col0, col1)

        if match_id >= min_index and match_id <= max_index:
            print(f"{col_name}0: {col0},\n{col_name}1: {col1},\nmatch: {match_id}%\n")

            id.append(col0)
            id.append(col1)

        idx += 1
    print(f"---\nAlgo: Partial Ratio|min param:{min_index}|max param:{max_index}")

    return set(id)


def fuzzypm(df, column, min_index=80, max_index=100):
    """Partial ratio function for string matching using fuzzy search. Good for multiple substrings.

    Args:
        df (_pd.DataFrame_): pandas dataframe containing the corresponding column.
        column (_str_): the column to be searched; string.
        min_index (int, optional): min fuzzy index to match. Defaults to 80.
        max_index (int, optional): min fuzzy index to match. Defaults to 100.
    """
    col_name = str(column)
    id = []
    idx = 0

    for i in df[column][1:]:
        col0 = df[column][idx]
        col1 = i
        match_id = fuzz.partial_ratio(col0, col1)

        if match_id >= min_index and match_id <= max_index:
            print(f"{col_name}0: {col0},\n{col_name}1: {col1},\nmatch: {match_id}%\n")

            id.append(col0)
            id.append(col1)

        idx += 1
    print(f"---\nAlgo: Partial Ratio|min param:{min_index}|max param:{max_index}")

    return set(id)
