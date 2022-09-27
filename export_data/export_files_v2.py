import glob
import os
import csv


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

    def _data_to_csv(self, files):
        total_header = set()
        for file in files:
            with open(file) as in_csv:
                reader = csv.reader(in_csv)
                in_header = next(reader, None)
                in_csv.close()

            inter_header = total_header.intersection(set(in_header))
            total_header.symmetric_difference_update(set(in_header))
            total_header.update(inter_header)

        total_header = list(total_header)
        print('Total header: ', total_header)

        with open(self._out_file,'w') as out_csv:
            writer = csv.DictWriter(out_csv, fieldnames=total_header)
            writer.writeheader()

            for file in files:
                with open(file) as in_csv:
                    reader = csv.DictReader(in_csv)
                    for row in reader:
                        if any(field.strip() for field in row):
                            writer.writerow(row)
                    in_csv.close()
            out_csv.close()

    def _data_to_json(self, files):
        print('To be done in a future!')


    def _data_to_xml(self, files):
        print('To be done in a future!')


    def _data_to_sql_light(self, files):
        print('To be done in a future!')


    def processing(self):
        """
        Processing input files. All parameters are fields of the object
        """
        result_df = None
        files = glob.glob(self._in_path + os.sep + '*.csv')
        if not files:
            raise EmptyInputFolder("Files not found")

        export_func = {
            self._export_method == 'csv':   self._data_to_csv,
            self._export_method == 'json':  self._data_to_json,
            self._export_method == 'xml':   self._data_to_xml,
            self._export_method == 'sql_l': self._data_to_sql_light
        }[True]
        export_func(files)
