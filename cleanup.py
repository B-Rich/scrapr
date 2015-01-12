import csv
import sys
import string

def clean_data(str):
    return str.replace(',MENU','')

def choose(input_array):
    output = []
    rowlen = len(input_array[0])

    for col in range(rowlen):
        curval = ''

        for row in input_array:
            if len(row[col]) > len(curval):
                curval = row[col]

        # clean up shitty data
        curval = clean_data(curval)

        output.append(curval)

    return output

if __name__ == '__main__':
    raw_data = {}

    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    bad_numbers = ['(888)', '(855)', '(844)', '(833)', '(822)', '(811)', '(866)', '(877)', '(900)', '(800)',]

    for row in reader:
        all_chars = string.maketrans('','')
        nodigs = all_chars.translate(all_chars, string.digits)
        number = row[0].translate(all_chars, nodigs)

        if len(number) == 0:
            continue

        bad_number = False

        for bno in bad_numbers:
            if bno in row[0]:
                bad_number = True

        if bad_number == True:
            continue

        new_row = [row[0], clean_data(row[3]), row[1], row[5], row[4], clean_data(row[3]), row[2],]

        if number in raw_data:
            raw_data[number].append(new_row)
            continue

        raw_data[number] = [new_row,]

    final_data = []

    for row in raw_data:
        if len(raw_data[row]) == 1:
            final_data.append(raw_data[row][0])
            pass
        else:
            final_data.append(choose(raw_data[row]))

    final_data = sorted(final_data, key=lambda row: row[1])

    for row in final_data:
        writer.writerow(row)