import sys
import os
import json

def extract_name(metadata_file):
    return metadata_file.split('.')[0]

def extract_values(filename, path):
    metadata = []

    for column in read_lines(filename, path):
        if column:
            values = column.split('\t')
            metadata.append((values[0], values[1], values[2]))

    return metadata

def read_lines(filename, path):
    file = open(os.path.join(path, filename), 'rt')
    line = file.read().split('\n')
    file.close()
    return line

def main(dir):
    meta = {}
    ids  = {}
    path = '{}/data/meta-data'.format(dir)

    for metadata_file in os.listdir(path):
        table_name = extract_name(metadata_file)
        attributes = extract_values(metadata_file, path)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        ids[identifier] = table_name

    for key, values in meta.items():
        for value in values:
            if value[0] in ids:
                # Value cannot be first key
                if not value[0] == meta[key][0][0]:
                    print("{} | {}".format(key, value[0]))

    # for key, values in meta.items():
    #     print('\n')
    #     print('Entities {}'.format(key))
    #     print('Column | Type | Description')
    #     for value in values:
    #         print('{} | {} | {}'.format(value[0], value[1], value[2]))

def test_extract_data(path):
    data = open(path, 'rt')
    meta_data = []

    for line in data:
        line_data = line.split('\t')
        meta_data.append(
            (line_data[0],
            line_data[1],
            line_data[2])
        )

    data.close()
    return meta_data


if __name__ == '__main__':
    # print(test_extract_data('saida/data/meta-data/Instituicao.txt'))
    main(sys.argv[1])