import pandas as pd


def merge_excel_files(file_list, output_file):
    """
    Merge multiple Excel files into a single Excel file.
    """

    dataframes = []

    for file in file_list:
        df = pd.read_excel(file)
        dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)

    merged_df.to_excel(output_file, index=False)

    print("Excel files merged successfully")
    print(f"Output file: {output_file}")


def main():

    files = [
        r"path_to_file1.xlsx",
        r"path_to_file2.xlsx",
        r"path_to_file3.xlsx",
    ]

    output_file = r"path_to_output\Merged_File.xlsx"

    merge_excel_files(files, output_file)


if __name__ == "__main__":
    main()
