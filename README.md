# A concatenation of CSV files into a one file.
## Output
- XML (to be done)
- CSV
- JSON (to be done)
- SQLlite3 (to be done)

## Prepare
```bash
python3 -m venv test or python -m venv test
git clone https://github.com/yegorovev/data_processing.git
cd test
source bin/activate
pip install -r data_processing/requirements.txt
```
## Commands (as examples)
### Help
```bash
(test) $ python main.py -h
usage: main.py [-h] [-i IN_PATH] [-o OUT_FILE] [-e {csv,json,xml,sql_l}]

A concatenation of CSV files into a DataSet. Saving DataSet into a file

optional arguments:
  -h, --help            show this help message and exit
  -i IN_PATH, --in IN_PATH
                        Path of incoming files. Default: <Here will your path>
  -o OUT_FILE, --out OUT_FILE
                        Path of export file. Default: <Here will your path>/result.csv
  -e {csv,json,xml,sql_l}, --exp {csv,json,xml,sql_l}
                        Export type (CSV, JSON, XML, SQLite3). Values: csv,json,xml,sql_l. Default: csv
```
### Data export
```bash

python main.py -i input -o output/out.csv -e csv
python main.py -i input -o output/out.json -e json
python main.py -i input -o output/out.xml -e xml
python main.py -i input -o output/out.sqllite -e sql_l
```
### Tests
```bash
mkdir output
python -m pytest
```
