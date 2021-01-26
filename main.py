import pandas as pd


def get_state(latitude: float, longitude: float):
    df_info = pd.read_csv('data/st_city.csv')
    df_info['control_lat'] = abs(df_info['latitude']-latitude)
    df_info['control_lon'] = abs(df_info['longitude']-longitude)
    df_info['control_distance'] = abs(
        df_info['control_lat']+df_info['control_lon'])
    control_distance_min = df_info['control_distance'].min()

    print(df_info.nsmallest(5, 'control_distance'))
    print(df_info['control_distance'].min())

    uf = (
        df_info[df_info['control_distance'] ==
                control_distance_min]['uf'].values[0]
    )
    return uf


#! Only test
# latitude = -23.46
# longitude = -46.2
# get_state(latitude, longitude)
