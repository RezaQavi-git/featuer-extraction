import os
import pandas as pd

from .indicators.adx import adx
from .indicators.aroon import aroon

from .indicators.bb import bb
from .indicators.wr import wr
from .indicators.SR import SR
from .indicators.cci import cci
from .indicators.ema import ema
from .indicators.mfi import mfi
from .indicators.rsi import rsi
from .indicators.sma import sma
from .indicators.macd import macd
from .indicators.stoch import stoch
from .indicators.trend import trend
from .indicators.ichimoku import ichimoku

from .utils.config import DURATION, EXPORTS_FOLDER, FILE_PATH, GET_URL, WRITE_FILE_PATH

coins = [
    'BTCUSDT',
    'ETHUSDT',
    'ADAUSDT'
]

functions = [
    adx,
    aroon,
    bb,
    cci,
    # ema,
    # ichimoku,
    # macd,
    mfi,
    rsi,
    # sma,
    # stoch,
    #wr,
    # trend,
    # SR
]

def fill_nan(df):
    return df.fillna(0)


def write_to_file(df, file_name):
    if not os.path.exists(EXPORTS_FOLDER):
        os.mkdir(EXPORTS_FOLDER)
    fullname = os.path.join(EXPORTS_FOLDER, file_name)   
    df.to_csv(fullname, sep=',')

def load_dataframe(name):

        # # Read Data from url
        # # if you want use this project beside an external source, you can use this function
        # # for config, see config.py
    # response = requests.get(GET_URL.format(name, DURATION))
    # csv_attached = response.content.decode('utf-8')
    # data = pd.read_csv(io.StringIO(csv_attached))
    # df = pd.DataFrame(data)

    # return df

        # Read data locally
        # To run locally, you can placed your files near main file, and set configs in config.py
        # then run and this project will read files and return result 
    data= pd.read_csv(FILE_PATH.format(name, DURATION))
    df = pd.DataFrame(data)

    return df

def create_features_dataframe(df):
    features_df = pd.DataFrame()
    df_list = []

    for i in range(len(functions)):
        df_ = (functions[i](df))
        df_list.append(df_)

    features_df = pd.concat(df_list, axis=1)

    return features_df


def main(df):
    # print('Start extrarting features : ...')
    # for c in coins:
        # print('\t Strat {0} feature extraction . . . '.format(c))
        # df = load_dataframe(c)

    features = create_features_dataframe(df)
    extracted_df = pd.concat([df, features], axis=1)

    return extracted_df
        # write_to_file(extracted_df, WRITE_FILE_PATH.format(c, DURATION))
        # print('\t Stop {0} feature extraction.You can find result in this path : {1}'.format(c, EXPORTS_FOLDER + '/' + WRITE_FILE_PATH.format(c, DURATION)))

    # print('End of extraction. enjoy :)')

def extract(df):
    return main(df)
