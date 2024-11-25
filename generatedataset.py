import csv 
import random
from faker import Faker

fake=Faker()

records_needed=2000

output_file="dataset.csv"


data=[
    {
        "Name": fake.name(),
        "Age": fake.random_int(min=18, max=107),
        "Email": fake.email().replace("\n",","),
        "Addrress":fake.address(),
        "Country": fake.country(),
        # "Department": fake.department(),
        "Company": fake.company(),
    }
    for _ in range(records_needed)
]

with open(output_file, mode="w", newline="", encoding="utf=8") as file:
    writer=csv.DictWriter(file,fieldnames=["Name","Age","Email","Addrress","Country","Company"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset with {records_needed} records saved to {output_file}")