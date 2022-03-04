import pandas as pd

# Read the dataset for ukrainian checkpoint data
def get_data():
    # TODO: Replace directory with your own
    directory = 'C:\\Users\\20201242\\Documents\\Ukraine\\ukraine_app\\datasets\\'
    # Read the excel file data with checkpoint details
    df = pd.read_excel(directory + "hk_checkpoint.xlsx", sheet_name = "Border Crossings")
    # df = pd.read_excel(directory + "ukraine_checkpoint.xlsx", sheet_name = "Border Crossings")
    # Create a column with tuple consisting of lagitude and longtitude
    df['coordinates'] = list(zip(df.Lat, df.Long))
    return df