from pprint import pprint
import csv
import re
from collections import defaultdict


with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    first_result = []
    contacts_dict = {}
    contacts_dict_1 = {}
    final_result = []

    for item in contacts_list:
        sub_list = []
        for elm in item[0:3]:
            sub_list.extend(elm.split())
        sub_list.extend(item[3:])
        first_result.append(sub_list)

    for item in first_result:
        pattern_phone = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s?)(\d*)(\-?)(\d*)(\-?)(\d*)(\s?(\(?)(доб.)\s?(\d*)(\)?))*'
        pattern_sub = r'+7(\4)\7\9\11 \14\15'
        result = re.sub(pattern_phone, pattern_sub, item[5])
        item[5] = result
        name = item[:3]
        info = item[4:]

        if tuple(item[:2]) not in contacts_dict:
            contacts_dict[tuple(item[:2])] = item[2:]
        else:
            contacts_dict_1[tuple(item[:2])] = item[2:]

        dd = defaultdict(list)
    for key in set(list(contacts_dict_1.keys()) + list(contacts_dict.keys())):
        if key in contacts_dict:
            dd[key].append(contacts_dict[key])
        if key in contacts_dict_1:
            dd[key].append(contacts_dict_1[key])

    for key, value in dd.items():
        a = []
        a.extend(key)
        for info in value:
            for i in info:
                if i not in a:
                    a.append(i)
        final_result.append(a)

    pprint(sorted(final_result))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(sorted(final_result))