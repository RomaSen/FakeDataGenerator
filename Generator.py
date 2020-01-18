import sys
import random
import string
from data import dictionary


# num_rec - non-negative integer
# num_er - non-negative
# region -  RU,BY,US

# Generating phone number
def generate_number(codes, region):
    code = random.choice(codes)
    number = str(random.randint(1111111, 9999999))
    if region == 'RU':
        return '+8' + code + number
    elif region == 'BY':
        return '+375' + code + number
    else:
        return '+1' + code + number


# Generating address
def generate_address(cities, streets, region):
    city = random.choice(cities)
    street = random.choice(streets)
    house_num = str(random.randint(1, 170))
    if region != 'US':
        house_num += random.choice(['', 'A', 'Б']) + random.choice(['', '/1', '/2', '/3'])
        return city + ' ' + street + ' ' + house_num + ' '
    else:
        return city + ' ' + street + ' ' + house_num + ' '


# Generating address
def generate_fullname(region):
    main_info = dictionary[region]
    if region != 'US':
        full_name = random.choice(main_info[0]) + ' ' + random.choice(main_info[1]) + ' ' + random.choice(main_info[2])
        return full_name
    else:
        full_name = random.choice(main_info[0]) + ' ' + ' ' + random.choice(main_info[1])
        return full_name


# Unite all data
def unite_data(region):
    main_info = dictionary[region]
    if region != 'US':
        phone_number = generate_number(main_info[5], region)
        address = generate_address(main_info[3], main_info[4], region)
    else:
        phone_number = generate_number(main_info[4], region)
        address = generate_address(main_info[2], main_info[3], region)
    full_name = generate_fullname(region)
    return [full_name, phone_number, address]


# Add some errors [if it needed]
def add_error(record, number_of_mistakes):
    actions = [add_char, delete_char, replace_char]
    for i in range(0, int(number_of_mistakes)):
        choose_part = random.randint(0, 2)
        data = record[choose_part]
        action = random.choice(actions)
        record[choose_part] = action(data, random.randint(0, len(data)))
    return record


def replace_char(data, index):
    alphabet = string.ascii_lowercase
    return data[:index] + random.choice(alphabet) + data[index + 1:]


def add_char(data, index):
    alphabet = string.ascii_lowercase
    return data[:index] + random.choice(alphabet) + data[index:]


def delete_char(data, index):
    return data[:index] + '' + data[index + 1:]


# Creating records with errors
def create_record_with_error(number_of_errors, region):
    record = unite_data(region)
    return add_error(record, number_of_errors)


def generate_records_with_low_chance_mistake(number_of_records, region, number_of_mistake):
    record_count_with_error = int(number_of_records) * number_of_mistake
    for i in range(0, number_of_records):
        if i > record_count_with_error:
            record = unite_data(region)
            print(record[0] + ' ' + record[1] + ' ' + record[2])
        else:
            record = create_record_with_error(number_of_records, region)
            print(record[0] + ' ' + record[1] + ' ' + record[2])


def generate_records_with_mistakes(number_of_records, region, number_of_mistakes):
    error_count = int(number_of_mistakes)
    for i in range(0, number_of_records):
        record = create_record_with_error(error_count, region)
        print(record[0] + ' ' + record[1] + ' ' + record[2])


def generate_ideal_records(num_rec, region):
    for i in range(0, num_rec):
        record = unite_data(region)
        print(record[0] + ' ' + record[1] + ' ' + record[2])


def start_generation(num_rec, region, num_er):
    if num_rec > 0 and num_er >= 0:
        if num_er == 0:
            generate_ideal_records(num_rec, region)
        elif num_er < 1:
            generate_records_with_low_chance_mistake(num_rec, region, num_er)
        else:
            generate_records_with_mistakes(num_rec, region, num_er)
    else:
        print("Some error")


# Launch point
if __name__ == "__main__":
    num_rec = int(sys.argv[1])
    region = sys.argv[2]
    num_er = float(sys.argv[3])
    start_generation(num_rec, region, num_er)
