import argparse
import os
from export_data.export_files_v2 import Importer


if __name__ == '__main__':
    in_path = os.getcwd() + os.sep + 'input'
    out_file = os.sep.join([os.getcwd(), 'output', 'result.csv'])

    parser = argparse.ArgumentParser(
        description='A concatenation of CSV files into a DataSet. Saving DataSet into a file')
    parser.add_argument('-i', '--in',
                        dest='in_path',
                        help='Path of incoming files. Default: ' + in_path,
                        default=in_path)
    parser.add_argument('-o', '--out',
                        dest='out_file',
                        help='Path of export file. Default: ' + out_file,
                        default=out_file)
    parser.add_argument('-e', '--exp',
                        dest='export_type',
                        help='Export type (CSV, JSON, XML, SQLite3). Values: csv,json,xml,sql_l.  Default: csv',
                        choices=['csv', 'json', 'xml', 'sql_l'], default='csv')

    args = parser.parse_args()
    importer = Importer(args.in_path, args.out_file, args.export_type)
    importer.processing()
    print('File ' + args.out_file + ' was created.')