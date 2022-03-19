from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    print(contacts_list)
    new_list = []
    new_list.append(contacts_list[0])

    for item in contacts_list:
        pat_name = r'([А-Я][а-я]+)(\'?,?)(\s*)(\'?)([А-Я][а-я]+)(\'?,?)(\s)*(\'?)([А-Я][а-я]+)*'
        pat_org = r'ФНС|Минфин'
        pat_pos = r'\b[a-zа-я]+(\s)(\s*)(\w*)(\s*)(\W*)(\w*)(\s*)(\w*)(\s*)(\w*)(\s*)(\w*)'
        pat_phone_add = r'(\+7|8)(\s+)*(\(*)(\d{3})(\)*)(\s*|\-*)(\d+)(\-*)(\d+)(\-*)(\d+)(,*\s*)(\(*доб.\s*)(\d+)(\)*)'
        pat_phone = r'(\+7|8)(\s+)*(\(*)(\d{3})(\)*)(\s*|\-*)(\d+)(\-*)(\d+)(\-*)(\d+)[^доб.]'
        pat_phone_1 = r'+7(\4)\7\9\11 доб.\14'
        pat_phone_2 = r'+7(\4)\7\9\11'
        pat_email = r'([a-zA-Z\.0-9]+@\w+.\w+)'

        a = r'\+7\(\d+\)\d+(\s*доб\.\d+)*'
        a_2 = r'\+7\(\d+\)\d+'

        name = re.search(pat_name, str(item))
        organisation = re.search(pat_org, str(item))
        position = re.search(pat_pos, str(item))
        phone_add = re.search(pat_phone_add, str(item))
        phone = re.search(pat_phone, str(item))

        phone_ad_new = re.sub(pat_phone_add, pat_phone_1, str(phone_add))
        phone_new = re.sub(pat_phone, pat_phone_2, str(phone))
        p = re.search(a, phone_ad_new)
        p_2 = re.search(a_2, phone_new)
        email = re.search(pat_email, str(item))

        if name:
            if name.group(1) and name.group(5) not in new_list:
                new_list.append(name.group(1))
                new_list.append(name.group(5))
                new_list.append(name.group(9))
                new_list.append(organisation.group(0))
            if position:
                new_list.append(position.group(0))
            if p:
                new_list.append(p.group(0))
            if p_2:
                new_list.append(p_2.group(0))
            if email:
                new_list.append(email.group(0))

    pprint(new_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list)