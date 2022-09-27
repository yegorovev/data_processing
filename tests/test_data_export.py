from export_data.export_files import Importer
import os
import pandas as pd


def test_importer_csv():
    in_path = os.getcwd() + os.sep + 'input'
    out_file = os.sep.join([os.getcwd(), 'output', 'result.csv'])
    importer = Importer(
        in_path=in_path,
        out_file=out_file,
        export_method='csv'
    )
    importer.processing()
    df = pd.read_csv(out_file)

    assert len(df.index) == 6


def test_importer_json():
    in_path = os.getcwd() + os.sep + 'input'
    out_file = os.sep.join([os.getcwd(), 'output', 'result.json'])
    importer = Importer(
        in_path=in_path,
        out_file=out_file,
        export_method='json'
    )
    importer.processing()
    df = pd.read_json(out_file)

    assert len(df.index) == 6


def test_importer_xml():
    in_path = os.getcwd() + os.sep + 'input'
    out_file = os.sep.join([os.getcwd(), 'output', 'result.xml'])
    importer = Importer(
        in_path=in_path,
        out_file=out_file,
        export_method='xml'
    )
    importer.processing()
    df = pd.read_xml(out_file)

    assert len(df.index) == 6
