import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_project.settings')
django.setup()

from booking.models import Destination

def populate():
    destinations = [
        {
            'title': 'Santorini Getaway',
            'description': 'Experience the breathtaking views, white-washed buildings, and blue-domed churches in Oia. Enjoy spectacular sunsets and romantic dinners by the sea. Perfect for couples and honeymooners.',
            'location': 'Santorini, Greece',
            'price_per_person': 1200.00,
            'duration_days': 5,
            'is_featured': True
        },
        {
            'title': 'Bali Tropical Escape',
            'description': 'Immerse yourself in lush jungles, ancient temples, and beautiful beaches. Reconnect with nature, enjoy world-class surfing, and relax in luxurious private villas.',
            'location': 'Bali, Indonesia',
            'price_per_person': 850.00,
            'duration_days': 7,
            'is_featured': True
        },
        {
            'title': 'Swiss Alps Adventure',
            'description': 'A spectacular journey through the snowy peaks of the Swiss Alps. Ski down world-class slopes, enjoy hot cocoa in a cozy chalet, and ride the scenic Glacier Express.',
            'location': 'Zermatt, Switzerland',
            'price_per_person': 2100.00,
            'duration_days': 6,
            'is_featured': True
        },
        {
            'title': 'Kyoto Cultural Tour',
            'description': 'Discover the historic heart of Japan. Visit breathtaking temples, stroll through serene bamboo groves, and experience traditional tea ceremonies.',
            'location': 'Kyoto, Japan',
            'price_per_person': 1500.00,
            'duration_days': 8,
            'is_featured': False
        },
        {
            'title': 'Machu Picchu Trek',
            'description': 'Hike the iconic Inca Trail and find yourself standing above the clouds at the mysterious Lost City. A challenging but deeply rewarding cultural and historical journey.',
            'location': 'Cusco, Peru',
            'price_per_person': 1100.00,
            'duration_days': 4,
            'is_featured': False
        }
    ]

    for data in destinations:
        dest, created = Destination.objects.get_or_create(title=data['title'], defaults=data)
        if created:
            print(f"Created: {dest.title}")
        else:
            print(f"Already exists: {dest.title}")

if __name__ == '__main__':
    print("Populating database...")
    populate()
    print("Done.")
