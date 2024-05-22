# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"4827020","system":"multilex"},{"code":"4815020","system":"multilex"},{"code":"4813020","system":"multilex"},{"code":"74924020","system":"multilex"},{"code":"74923020","system":"multilex"},{"code":"4817020","system":"multilex"},{"code":"4822020","system":"multilex"},{"code":"95364020","system":"multilex"},{"code":"74925020","system":"multilex"},{"code":"95362020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lithium-and-other-mood-stabilisers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lithium-and-other-mood-stabilisers-chronosphere---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lithium-and-other-mood-stabilisers-chronosphere---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lithium-and-other-mood-stabilisers-chronosphere---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
