import pandas as pd


def build_columns():
    columns = ['pid']
    for i in range(1, 501):
        columns.append('trackuri_%s' % i)

    return columns


def build_output(df_list, id_cloumn, song_column):
    output = pd.DataFrame(columns=build_columns())
    for df in df_list:
        output = output.append(format_output(df, id_cloumn, song_column))

    return output


def format_output(df, id_cloumn, song_column):
    columns = build_columns()[1:501]
    output = df
    output['columns'] = columns
    output = output.pivot(index=id_cloumn, columns='columns', values=song_column)
    output['pid'] = output.index
    output = output[build_columns()]

    return output


def output_submission(df, file_name, team_name, contact_information, path='submissions/', challenge_track='main'):
    file = path + file_name

    first_row = pd.DataFrame(columns=build_columns())
    first_row.loc[0] = build_first_row(team_name, contact_information, challenge_track)

    output = pd.concat([first_row, df])
    output = output[build_columns()]
    output = output.set_index('pid')
    output.to_csv(file)


def build_first_row(team_name, contact_information, challenge_track='main'):
    row = ['team_info', challenge_track, team_name, contact_information]
    for i in range(4, 501):
        row.append(None)

    return row
