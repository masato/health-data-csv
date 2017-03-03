# -*- coding: utf-8 -*-

from lxml import objectify
import pandas as pd
from pandas import DataFrame
from dateutil.parser import parse
from datetime import datetime
import zipfile
import argparse
import sys, os

def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        default='書き出した.zip',
                        type=str,
                        help='zipファイル名 (書き出した.zip)')
    parser.add_argument('-s', '--start',
                        action='store',
                        default='2016-01-01',
                        type=str,
                        help='開始日 (2016-12-01)')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print('zipファイル名を指定してください。')
        parser.print_help()
        sys.exit(1)

    zipfile.ZipFile(args.file).extractall()

    parsed = objectify.parse(open('apple_health_export/書き出したデータ.xml'
                                  .encode('utf-8').decode('cp437')))

    root = parsed.getroot()

    headers = ['type', 'unit', 'startDate', 'endDate', 'value']

    data = [({k: v for k, v in elt.attrib.items() if k in headers})
            for elt in root.Record]

    df = DataFrame(data)
    df.index = pd.to_datetime(df['startDate'])

    # 歩数だけ
    steps_tmp = df[df['type'] == 'HKQuantityTypeIdentifierStepCount']
    steps = steps_tmp['value'].astype(float)

    # 開始日が条件にある場合スライス
    if args.start:
        steps = steps.loc[args.start:]

    # 日別にグループ化して集計
    steps_sum = steps.groupby(pd.TimeGrouper(freq='D')).sum()

    steps_sum.T.to_csv('./steps_{0}.csv'.format(datetime.now().strftime('%Y%m%d%H%M%S')),
                       index=False, float_format='%.0f')

if __name__ == '__main__':
    main(sys.argv[1:])
