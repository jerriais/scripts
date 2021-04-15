import csv
from faker import Faker
import datetime

def datagenerate(records, headers, files):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
#    fake2 = Faker(['en_US', 'zh_CN', 'ja_JP', 'ar_AA', 'ru_RU', 'sv_SE'])

    # Faker.seed(4321)   # seed can be used to de-randomize the data generation
    for i in range(files):
        index = i+1
        filename =  "DQIX-test-data-%s.csv" % index
        with open(filename, 'wt') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            writer.writeheader()
            print("CSV generation of file ", index, " started")
            for j in range(records):
                # full_name = fake.name()
                # FLname = full_name.split(" ")
                # Fname = FLname[0]
                # Lname = FLname[1]
                # domain_name = "@testDomain.com"
                # userId = Fname + "." + Lname + domain_name
                cardinality = ""
                
                def card ():          
                    if j+1 > records * 0.06:
                        return "str of about thirty five characters"
                    else:
                        return fake.text(max_nb_chars=43) # generates cells with avg 35 characters
                        
                writer.writerow({
                        # "Email Id" : userId,
                        "ID" : j+1,
                        "Cardinality1" : card(),
                        "Cardinality2" : card(),
                        "Cardinality3" : card(),
                        "Cardinality4" : card(),
                        "Cardinality5" : card(),
                        "Cardinality6" : card(),
                        "Cardinality7" : card(),
                        "Cardinality8" : card(),
                        "Cardinality9" : card(),
                        "Cardinality10" : card(),
                        "Cardinality11" : card(),
                        "Cardinality12" : card(),
                        "Prefix" : fake.prefix(),
                        "Name": fake.name(),
                        "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                        "Phone Number" : fake1.phone_number(),
                        "Additional Email Id": fake.email(),
                        "Address" : fake.address(),
                        "Zip Code" : fake.zipcode(),
                        "City" : fake.city(),
                        "State" : fake.state(),
                        "Country" : fake.country(),
                        "Year":fake.year(),
                        "Time": fake.time(),
                        # "Link": fake.url(),
                        "Text1": fake.word(),
                        "Text2": fake.word(),
                        "Text3": fake.word(),
                        "Text4": fake.word(),
                        "Text5": fake.word(),
                        # "String": fake.pystr(min_chars=35, max_chars=35),
                        })

if __name__ == '__main__':
    records = 50
    files = 2
    headers = ["ID", "Cardinality1",  "Cardinality2", "Cardinality3", "Cardinality4", "Cardinality5", "Cardinality6", "Cardinality7", "Cardinality8", "Cardinality9", "Cardinality10", "Cardinality11", "Cardinality12","Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id", "Address", "Zip Code", "City","State", "Country", "Year", "Time", "Text1", "Text2", "Text3", "Text4", "Text5"]
    datagenerate(records, headers, files)
    print("CSV generation complete!")

