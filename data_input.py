from os import path
import sys
import pandas as pd 
class DataInput:
    supported_file_extensions = [
        '.csv',
    ]
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data
    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.argv[1])
            if file_extension == "":
                raise SystemExit(f"Provide the DATASET name (with extension).")
            if file_extension not in self.supported_file_extensions:
                raise SystemExit(f"This file extension is not supported.")
        except IndexError:
            raise SystemExit(f"Provide the DATASET name (with extension).")
        try:
            data = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is EMPTY")
        except FileNotFoundError:
            raise SystemExit(f"File doesn't exist")
        data = self.change_to_lower_case(data)
        return data