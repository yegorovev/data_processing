import glob
import os
import pandas as pd
import sqlite3


class EmptyInputFolder(Exception):
    pass


class Importer:
    """
    Class for grab data from files and export data to file
    """
    _in_path = ''
    _out_file = ''
    _export_type = ''

    def __init__(self, in_path, out_file, export_method):
        self._in_path = in_path
        self._out_file = out_file
        self._export_method = export_method

    def _export(self, **kwargs):
        """
        Wrapper for export
        """
        if self._export_method == 'sql_l':
            kwargs['func'](kwargs['data'])
        else:
            kwargs['func'](kwargs['path_or_buffer'], index=kwargs['index'])

    def _data_to_sql_light(self, data):
        """
        Saving Data Frame into SQLite
        @param data: Input DataFrame
        """
        conn = sqlite3.connect(self._out_file)
        data.to_sql("TOTAL_DATA", conn, if_exists="replace")
        conn.commit()
        conn.close()

    def processing(self):
        """
        Processing input files. All parameters are fields of the object
        """
        result_df = None
        files = glob.glob(self._in_path + os.sep + '*.csv')
        if not files:
            raise EmptyInputFolder("Files not found")

        for file in files:
            if self._out_file == file:
                continue
            result_df = pd.concat([result_df, pd.read_csv(file)], ignore_index=True)

        export_func = {
            self._export_method == 'csv':   result_df.to_csv,
            self._export_method == 'json':  result_df.to_json,
            self._export_method == 'xml':   result_df.to_xml,
            self._export_method == 'sql_l': self._data_to_sql_light
        }[True]
        self._export(func=export_func,
                     path_or_buffer=self._out_file,
                     index=self._export_method == 'json',
                     data=result_df)
