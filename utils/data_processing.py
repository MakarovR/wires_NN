def convert_df_to_list(dataframe):
    test_x = []
    test_y = []
    for i in range(len(dataframe)):
        test_x.append([float(dataframe.iloc[i]['U1a']), float(dataframe.iloc[i]['U1b']),
                       float(dataframe.iloc[i]['U1c']),
                       float(dataframe.iloc[i]['Uz']), float(dataframe.iloc[i]['Up']),
                       float(dataframe.iloc[i]['Un']),
                       float(dataframe.iloc[i]['KdUa']), float(dataframe.iloc[i]['KdUb']),
                       float(dataframe.iloc[i]['KdUc']),
                       float(dataframe.iloc[i]['KdU'])])
        test_y.append(float(dataframe.iloc[i]['OZZ']))
    return test_x, test_y