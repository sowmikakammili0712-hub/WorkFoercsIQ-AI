import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

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
cost_mapping = {
    "Junior": 15,
    "Mid": 25,
    "Senior": 40
}

categories = [
    "Login Issue",
    "Billing",
    "Domain Management",
    "Hosting",
    "Website Builder",
    "Email Support"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Resolved",
    "Resolved",
    "Resolved",
    "Resolved",
    "Open"
]
queues = [
    "Customer Support",
    "Billing Support",
    "Technical Support",
    "Domain Support",
    "Hosting Support"
]

tiers = [
    "Tier1",
    "Tier2",
    "Tier3"
]
customer_regions = [
    "USA",
    "Canada",
    "UK",
    "Germany",
    "Australia",
    "India"
]

complexities = [
    "Low",
    "Medium",
    "High"
]

resolution_categories = [
    "Self-Service",
    "Agent Resolved",
    "Escalated Resolution",
    "Engineering Fix"
]
for i in range(100):
    experience = random.choice(
      experience_levels
    )

    agent = {
        "AgentID": f"AG{str(i+1).zfill(3)}",
        "AgentName": fake.name(),
        "Team": random.choice(teams),
        "Region": random.choice(regions),
        "ExperienceLevel": experience,
        "HireDate": fake.date_between(
            start_date="-5y",
            end_date="today"
             ),
        
        "AgentCostPerHour":
           cost_mapping[experience],

        "CapacityHoursPerWeek":
           random.choice(
             [35, 40, 45]
          ),

       "TargetTicketsPerWeek":
          random.choice(
           [50, 75, 100]
          ),

        "UtilizationTarget":
           random.choice(
            [75, 80, 85, 90]
           ),
    }

    agents.append(agent)

agents_df = pd.DataFrame(agents)
dim_agent = agents_df.copy()
dim_agent.to_csv(
    "02_Dataset/Dimensions/dim_agent.csv",
    index=False
)
dim_queue = pd.DataFrame({
    "QueueName": queues
})
dim_queue.to_csv(
    "02_Dataset/Dimensions/dim_queue.csv",
    index=False
)
dim_region = pd.DataFrame({
    "RegionName": customer_regions
})
dim_region.to_csv(
    "02_Dataset/Dimensions/dim_region.csv",
    index=False
)
date_range = pd.date_range(
    start="2025-01-01",
    end="2026-12-31"
)
dim_date = pd.DataFrame({
    "Date": date_range
})
dim_date["Year"] = dim_date["Date"].dt.year

dim_date["Month"] = dim_date["Date"].dt.month

dim_date["MonthName"] = dim_date["Date"].dt.strftime("%B")

dim_date["Quarter"] = (
    "Q"
    +
    dim_date["Date"].dt.quarter.astype(str)
)
dim_date.to_csv(
    "02_Dataset/Dimensions/dim_date.csv",
    index=False
)
agents_df["ActualTicketsHandled"] = np.random.randint(
    40,
    120,
    len(agents_df)
)
agents_df["ActualHoursWorked"] = round(
    agents_df["CapacityHoursPerWeek"]
    *
    np.random.uniform(
        0.7,
        1.1,
        len(agents_df)
    ),
    2
)
agents_df["UtilizationPercent"] = round(
    (
        agents_df["ActualHoursWorked"]
        /
        agents_df["CapacityHoursPerWeek"]
    ) * 100,
    2
)
agents_df["CostPerTicket"] = round(
    (
        agents_df["AgentCostPerHour"]
        *
        agents_df["ActualHoursWorked"]
    )
    /
    agents_df["ActualTicketsHandled"],
    2
)
print("\nAgent Sample:")
print(agents_df.head())
print("\nAgent Columns:")
print(agents_df.columns.tolist())
tickets=[]
for i in range(1000):
 
    created_date = fake.date_between(
     start_date="-180d",
     end_date="today"
)
    forecast_week = created_date.isocalendar()[1]

    forecast_month = created_date.strftime("%Y-%m")
    resolution_hours = round(
      random.uniform(1,48),
      2
)
    closed_date = (
     datetime.combine(
        created_date,
        datetime.min.time()
     )
     +
     timedelta(hours=resolution_hours)
)
    agent_ids = agents_df["AgentID"].tolist()
    ticket = {

        "TicketID": f"TKT{str(i+1).zfill(5)}",

        "Category": random.choice(categories),

        "Priority": random.choice(priorities),
        "ForecastWeek":
            forecast_week,

        "ForecastMonth":
            forecast_month,

        "CustomerRegion":
            random.choice(customer_regions),

        "TicketComplexity":
            random.choice(complexities),

        "ResolutionCategory":
            random.choice(resolution_categories
            ),

        "AssignedAgent":
             random.choice(agent_ids),

        "ResolutionHours":resolution_hours,

        "SLAHours":
            random.choice(
                [4,8,12,24]
            ),
            

        "Status":
            random.choice(statuses),
    
     "CreatedDate":created_date,


    "ClosedDate": 
    closed_date.date(),

     "Queue":
    random.choice(queues),

    "Tier":
    random.choice(tiers),

"EscalatedFlag":
    random.choice(
        [True, False]
    ),   

    }
    ticket["BacklogAge"] = (
    datetime.today().date()
    -
    ticket["CreatedDate"]
).days    
    ticket["SLAMet"] = (
    ticket["ResolutionHours"]
        <=
    ticket["SLAHours"]
    )
    tickets.append(ticket)

tickets_df = pd.DataFrame(tickets)

print("\nSample Data:")
print(agents_df.head())

print("\nTotal Agents Created:")
print(len(agents_df))

agents_df.to_csv(
    "02_Dataset/Sample/agents.csv",
    index=False
)

print("\nCSV Export Successful!")

tickets_df.to_csv(
    "02_Dataset/Sample/tickets.csv",
    index=False
)

print("\nTickets Export Successful!")
print("\nTicket Sample:")
print(tickets_df.head())

print("\nTotal Tickets:")
print(len(tickets_df))