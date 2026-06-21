import pandas as pd
import numpy as np
from faker import Faker
import random

print("===================================")
print("WorkForceIQ AI")
print("Enterprise Data Generator")
print("Version 0.1")
print("===================================")

fake = Faker()

random.seed(42)
np.random.seed(42)

print("Libraries Loaded Successfully!")

agents = []

teams = ["Tier1", "Tier2", "Tier3"]

regions = [
    "North America",
    "Europe",
    "APAC"
]

experience_levels = [
    "Junior",
    "Mid",
    "Senior"
]

for i in range(100):

    agent = {
        "AgentID": f"AG{str(i+1).zfill(3)}",
        "AgentName": fake.name(),
        "Team": random.choice(teams),
        "Region": random.choice(regions),
        "ExperienceLevel": random.choice(experience_levels),
        "HireDate": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    }

    agents.append(agent)

agents_df = pd.DataFrame(agents)

print("\nSample Data:")
print(agents_df.head())

print("\nTotal Agents Created:")
print(len(agents_df))

agents_df.to_csv(
    "02_Dataset/Sample/agents.csv",
    index=False
)

print("\nCSV Export Successful!")