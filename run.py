import sys
import os
import json

def extract_name(metadata_file):
    return metadata_file.split('.')[0]

def extract_values(filename, path):
    metadata = []

    for column in read_lines(filename, path):
        if column:
            metadata.append(tuple(column.split('\t')[:3]))

    return metadata

def read_lines(filename, path):
    file = open(os.path.join(path, filename), 'rt')
    line = file.read().split('\n')
    file.close()
    return line

def clean_worthless(object):
    key_dels = []
    for key, value in object.items():
        if not len(value):
            key_dels.append(key)
    for key in key_dels:
        del object[key]

def prompt():
    print('\nEnter the option')
    print('1 - List entities')
    print('2 - Display model of entities')
    print('3 - Display attributes by entity')
    print('4 - Display foreign key of entities')
    print('5 - Display relationship of entities')
    print('0 - Exit')
    return input('')

def main(dir):
    option        = None
    meta          = {}
    ids           = {}
    foreignkeys   = {}
    relationships = {}
    path          = '{}/data/meta-data'.format(dir)

    # Create meta
    for metadata_file in os.listdir(path):
        table_name = extract_name(metadata_file)
        attributes = extract_values(metadata_file, path)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        ids[identifier]  = table_name

    # Create relationships and foreignkeys
    for key, values in meta.items():
        foreignkeys[key]   = []
        relationships[key] = []
        for value in values:
            if value[0] in ids:
                # Value cannot be first key
                if not value[0] == meta[key][0][0]:
                    relationships[key].append(ids[value[0]])
                    foreignkeys[key].append(value[0])

    # Clean relationships and foreignkeys worthless
    clean_worthless(relationships)
    clean_worthless(foreignkeys)

    # Prompt interaction
    option = prompt()
    while option != '0':
        if option == '1':
            print('All entities \n--------------------')
            for key in meta.keys():
                print(key)
        elif option == '2':
            for key, values in meta.items():
                print('\nEntity: {}'.format(key))
                print('Attribute | Type | Description')
                for value in values:
                    print('{} | {} | {}'.format(value[0], value[1], value[2]))
                print('\n')
        elif option == '3':
            name = input('Enter name of entity: ')
            print('Attribute | Type | Description')
            for value in meta[name]:
                print('{} | {} | {}'.format(value[0], value[1], value[2]))
        elif option == '4':
            for key, values in foreignkeys.items():
                print('Entity: {}'.format(key))
                for value in values:
                    print('FK: {}'.format(value))
        elif option == '5':
            for key, values in relationships.items():
                print('Entity: {}'.format(key))
                for value in values:
                    print('relates to {}'.format(value))
        else:
            print('Option not found...\n')
        option = prompt()


if __name__ == '__main__':
    main(sys.argv[1])