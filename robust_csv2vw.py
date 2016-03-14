'Convert CSV file to VW format.'

import argparse
import csv


def construct_line(line, header):
    string_vw = "{0[0]} |".format(line)
    for j in range(len(header) - 1):
        string_vw += " {0}:{1}".format(header[j + 1], line[j + 1])
    string_vw += "\n"
    return string_vw

parser = argparse.ArgumentParser(description='Convert CSV to VW format.')
parser.add_argument("input_file", help="path to csv file")
parser.add_argument("output_file", help="path to output vw file")

args = parser.parse_args()

with open(args.input_file, encoding='utf-8') as input_file:
    with open(args.output_file, mode='a', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        header = next(reader)
        for row in reader:
            output_file.write(construct_line(row, header))
