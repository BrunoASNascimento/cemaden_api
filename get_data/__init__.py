import json
import requests
import pandas as pd
from datetime import datetime, timedelta


def get_data(state):

    url = "http://sjc.salvar.cemaden.gov.br/resources/graficos/interativo/getJson2.php"
    querystring = {'uf': state}
    headers = {
        'cache-control': 'no-cache',
        # 'postman-token': 'f94837f1-4702-93e4-8232-ed2c8728a989'
    }
    response = requests.request(
        'GET', url, headers=headers, params=querystring)

    data_df = json.loads(response.text)

    df = pd.DataFrame(data_df)

    #!Filter
    df['date'] = pd.to_datetime(
        df['datahoraUltimovalor'], format='%d/%m/%y %H:%M', errors='ignore').dt.tz_localize('UTC')
    date_now = pd.to_datetime(
        datetime.utcnow()-timedelta(minutes=20))
    df = df[df['date'] >= pd.Timestamp(date_now, tz="UTC")]

    # #!Parser
    # df['cidade'] = df['cidade'].str.title()
    # df['stationtime'] = df['date'].dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    df[['ultimovalor', 'acc1hr', 'acc3hr', 'acc6hr', 'acc12hr',
        'acc24hr', 'acc48hr', 'acc72hr', 'acc96hr']] = df[['ultimovalor', 'acc1hr', 'acc3hr', 'acc6hr', 'acc12hr',
                                                           'acc24hr', 'acc48hr', 'acc72hr', 'acc96hr']].replace('-', 0).astype(float)
    print(df)
    print(df.info())
    print(df[df['codibge'] == 3530607])

    # df['timestamp'] = df['date'].astype(np.int64) // 10**9
    # df['bucket'] = (df['ultimovalor']/0.2).round(0).astype(np.int64)
    # df.rename(columns=rename_dict, inplace=True)

    # df = df[columns].drop_duplicates()
    # df_info = pd.read_csv('data/stations_cemaden.csv')
    # data = upload_data(df, df_info)

    # return data


get_data('SP')
