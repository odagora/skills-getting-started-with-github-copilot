#!/usr/bin/env python3
"""
Script to populate MongoDB with initial activities data
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Sample activities data (same as the original hardcoded data)
activities_data = {
    # Sports related activities
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "lucas@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu", "ethan@mergington.edu"]
    },

    # Artistic activities
    "Art Club": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu", "liam@mergington.edu"]
    },
    "Drama Society": {
        "description": "Participate in theater productions and acting workshops",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
    },

    # Intellectual activities
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Fridays, 2:00 PM - 3:30 PM",
        "max_participants": 16,
        "participants": ["william@mergington.edu", "charlotte@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["benjamin@mergington.edu", "amelia@mergington.edu"]
    }
}


def populate_database():
    """Populate MongoDB with initial activities data"""
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        
        # Test the connection
        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB!")
        
        # Get database and collection
        db = client.mergington_high_school
        activities_collection = db.activities
        
        # Clear existing data
        activities_collection.delete_many({})
        print("🗑️  Cleared existing activities data")
        
        # Insert activities with activity name as the _id (key)
        documents_to_insert = []
        for activity_name, activity_data in activities_data.items():
            document = {
                "_id": activity_name,  # Use activity name as the key
                **activity_data  # Spread the activity data
            }
            documents_to_insert.append(document)
        
        # Insert all documents
        result = activities_collection.insert_many(documents_to_insert)
        print(f"📝 Successfully inserted {len(result.inserted_ids)} activities:")
        
        # Print all inserted activities
        for activity_name in result.inserted_ids:
            print(f"   - {activity_name}")
        
        # Verify the data
        print(f"\n📊 Database verification:")
        total_count = activities_collection.count_documents({})
        print(f"   Total activities in database: {total_count}")
        
        # Close the connection
        client.close()
        print("\n🎉 Database population completed successfully!")
        
    except ConnectionFailure:
        print("❌ Failed to connect to MongoDB. Make sure MongoDB is running.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    populate_database()
