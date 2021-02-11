import re
import shutil

emailRe = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
phoneRe = re.compile(r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
                     )

email_list = []
phone_number_list = []

with open("../assets/potential-contacts.txt", 'r') as file:
    file_data = file.readlines()

    for line in file_data:
        if phoneRe.search(line):
            found_phone_number = phoneRe.search(line)
            phone_number = found_phone_number.group()

            if len(phone_number.split('x')[0]) < 10:
                phone_number = '206-' + phone_number
            if len(phone_number) == 10:
                phone_number = phone_number[:3] + "-" + \
                    phone_number[3:6] + "-" + phone_number[6:]
            if len(phone_number) == 11:
                phone_number = phone_number[:7] + "-" + phone_number[7:]
            if '.' in phone_number:
                phone_number = phone_number.replace('.', '-')
            if '(' in phone_number or ')' in phone_number:
                phone_number = phone_number.strip('(')
                phone_number = phone_number.replace(')', '-')
            if '1-' in phone_number[:2] or '+1' in phone_number[:2]:
                phone_number = phone_number.strip('+1-')
                phone_number = phone_number.strip('1-')

            phone_number_list.append(phone_number)

        if emailRe.search(line):
            email = emailRe.search(line)
            email = email.group()
            email_list.append(email)

    for phone_number in phone_number_list:
        while phone_number_list.count(phone_number) > 1:
            phone_number_list.remove(phone_number)

    for email in email_list:
        while email_list.count(email) > 1:
            email_list.remove(email)

phone_number_list.sort()
email_list.sort()

with open('../assets/phone_numbers.txt', 'w+') as new_file:
    for phone_number in phone_number_list:
        new_file.write(f'{phone_number}\n')

with open('../assets/emails.txt', 'w+') as new_file:
    for email in email_list:
        new_file.write(f'{email}\n')
