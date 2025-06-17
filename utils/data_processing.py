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


def convert_second_df_to_list(dataframe):
    test_x = []
    test_y = []
    for i in range(len(dataframe)):
        test_x.append([float(dataframe.iloc[i]['I1a']), float(dataframe.iloc[i]['I1b']),
                       float(dataframe.iloc[i]['I1c']),
                       float(dataframe.iloc[i]['Iz']), float(dataframe.iloc[i]['Ip']),
                       float(dataframe.iloc[i]['In']),
                       float(dataframe.iloc[i]['KdIa']), float(dataframe.iloc[i]['KdIb']),
                       float(dataframe.iloc[i]['KdIc']),
                       float(dataframe.iloc[i]['KdI'])])
        test_y.append(float(dataframe.iloc[i]['OZZ']))
    return test_x, test_y
