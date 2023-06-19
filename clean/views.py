from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

services = [

    {
        "id": 1,
        "slug": "janitorial-and-office-cleaning-services",
        "title": "Janitorial and Office Cleaning Services",
        "description": "At Gevito Cleaning Services, we know that a clean and organized office environment plays a vital role in productivity and overall success. That's why we're here to provide top-notch office cleaning services that will transform your workspace into a pristine haven, allowing you and your employees to focus on what truly matters—your core business activities.\n\nOur dedicated team of cleaning professionals is well-versed in the art of office maintenance with meticulous attention to detail, we cover every aspect of cleaning, from dusting to vacuuming, mopping to sanitizing. No corner is left untouched, ensuring that your office space not only looks immaculate but also promotes a healthy and inspiring work environment.\n\nBut we don't stop at just cleanliness. We understand that your office is a reflection of your brand and values. That's why we go the extra mile to tailor our services to your specific needs, preferences, and schedule. Whether you require daily, weekly, or monthly cleaning, we've got you covered.\n\nOur flexible and customizable packages ensure that you receive the exact level of service your office deserves.\n\nAt Gevito Professional Cleaning services we take pride in our use of cutting-edge cleaning techniques and eco-friendly products. By staying up-to-date with industry advancements, we are able to deliver exceptional results while minimizing our environmental impact. You can have peace of mind knowing that your office is not only clean but also contributing to a greener and more sustainable future.",
        "images": ["/static/assets/images/janitorial.jpeg", "/static/assets/images/janitorial1.jpeg", "/static/assets/images/janitorial2.jpeg"]
    },
     {
         "id": 2,
         "slug": "expert-fumigation-and-pest-control-services",
        "title": "Expert Fumigation and Pest Control Services",
        "description": "At Gevito Professional Cleaning Services, we are dedicated to prioritizing the health and safety of our clients. Our exceptional fumigation and disinfection services specifically target high-contact areas to eliminate harmful bacteria, viruses, and pesky pests. With our safe and effective methods, we go the extra mile to sanitize surfaces, creating a clean and germ-free environment that gives you peace of mind.\n\nDon't let unwanted intruders compromise your space. Trust Gevito Cleaning Services to provide expert fumigation and pest control solutions that keep your environment safe and inviting. Contact us today to reclaim a pest-free and sanitized space for your peace of mind.",
        "images": ["/static/assets/images/pest.jpeg", "/static/assets/images/pest1.jpeg", "/static/assets/images/pest2.jpeg"]
    },
    {
        "id": 3,
        "slug": "premium-laundry-and-dry-cleaning-services",
        "title": "Premium Laundry and Drycleaning Services",
        "description": "At Gevito Cleaning Services, we understand that laundry and drycleaning can be time-consuming and burdensome. That's why we're here to take the load off your shoulders. Our impeccable laundry and drycleaning services ensure that your clothes are handled with utmost care, providing you with clean and neatly ironed garments.\n\nWith us, you can bid farewell to the hassles of laundry and enjoy more time for the important things in life.\n\nExperience the convenience and quality of Gevito Professional Cleaning Services. Contact us today to indulge in fresh, wrinkle-free clothes that make you feel confident and ready to conquer the day!",
        "images": ["/static/assets/images/laundry.jpeg", "/static/assets/images/laundry1.jpeg", "/static/assets/images/laundry2.jpeg"]
    },
    {
        "id": 4,
        "slug": "deep-cleaning-services",
        "title": "Deep Cleaning Services",
        "description": "At Gevito Cleaning Services, we understand that sometimes regular cleaning just isn't enough. That's where our exceptional deep cleaning services come in. We go the extra mile to provide a thorough and comprehensive cleaning experience that surpasses the surface level.\n\nWith our meticulous approach, we eliminate dirt, grime, and allergens from every nook and cranny, giving your space a complete refresh and leaving it truly spotless.\n\nOur deep cleaning services cover a wide range of areas, including:\n\n- Kitchen Revival: We tackle grease buildup, sanitize countertops, degrease appliances, and ensure your kitchen shines like new.\n\n- Bathrooms Rejuvenation: We remove stubborn stains, sanitize toilets, scrub tiles, and leave your bathrooms sparkling clean and fresh.\n\n- Floor Transformation: From carpets to hardwood, we deep clean and revitalize your floors, removing embedded dirt and restoring their original luster.\n\n- Dust and Allergen Removal: We pay special attention to dusting and removing allergens from furniture, vents, and hard-to-reach corners, ensuring a healthier environment.\n\n- Upholstery and Furniture Renewal: We revitalize your upholstery and furniture, treating stains, eliminating odors, and bringing back their vibrant appearance.\n\n- Window and Glass Brilliance: We achieve streak-free, crystal-clear windows and glass surfaces, enhancing natural light and the overall ambiance.\n\nNo matter the size or type of your space, our dedicated team of cleaning professionals will customize our deep cleaning services to meet your specific needs. We use industry-leading techniques, high-quality products, and attention to detail to ensure outstanding results.\n\nExperience the difference with Gevito Professional Cleaning Services. Contact us today to schedule a deep cleaning service and witness the total transformation of your space. Get ready to be amazed.",
        "images": ["/static/assets/images/bathroom.jpeg", "/static/assets/images/bathroom1.jpeg", "/static/assets/images/bathroom2.jpeg"]
    },
    {
        "id": 5,
        "slug": "expert-rug-and-upholstery-cleaning-services",
        "title": "Expert Rug and Upholstery Cleaning Services",
        "description": "At Gevito Cleaning Services, we understand the importance of clean and fresh rugs and upholstery in creating a welcoming and comfortable home. Our exceptional rug and upholstery cleaning services are designed to revitalize and restore the beauty of your cherished furniture and rugs, making them look and feel like new.\n\nOur team of skilled cleaning professionals utilizes specialized techniques and state-of-the-art equipment to ensure a thorough and effective cleaning process. We pay meticulous attention to detail, carefully treating and removing stains, dirt, allergens, and odours that have accumulated over time. With our expertise, your rugs and upholstery will regain their vibrant colours and freshness, enhancing the overall ambiance of your living spaces.\n\nWe cater to a wide range of fabrics and materials, from delicate silk and velvet to durable microfiber and leather. Our cleaning methods are tailored to the specific requirements of each item, ensuring the utmost care and protection throughout the cleaning process. You can trust us to handle your treasured belongings with the highest level of professionalism and respect.\n\nExperience the transformative power of our rug and upholstery cleaning services. Let us breathe new life into your beloved furniture and rugs, creating a clean, fresh, and inviting atmosphere in your home.",
        "images": ["/static/assets/images/rug.jpeg", "/static/assets/images/rug1.jpeg", "/static/assets/images/rug2.jpeg"]
    },

]

trainings = [

    {
        "id": 1,
        "slug": "dedicated-expertise",
        "title": "Dedicated Expertise",
        "description": "Your affiliated employee will become intimately familiar with your premises, allowing them to develop a deep understanding of your cleaning needs and preferences. They will consistently deliver top-quality services with meticulous attention to detail.",
        "images": ["/static/assets/images/training.jpeg", "/static/assets/images/janitorial1.jpeg", "/static/assets/images/janitorial2.jpeg"]
    },
     {
         "id": 2,
         "slug": "personal-approach",
        "title": "Personalized Approach",
        "description": "We recognize that every organization has unique cleaning requirements. With our affiliation program, your dedicated employee will work closely with you to create a customized cleaning plan that addresses your specific needs, ensuring maximum satisfaction. By taking the time to understand your organization's layout, workflow, and priorities, our affiliated employee will develop a deep understanding of your cleaning requirements. They will consider factors such as the size of your premises, the nature of your business, and any specific areas or items that require special attention.",
        "images": ["/static/assets/images/training.jpeg", "/static/assets/images/pest1.jpeg", "/static/assets/images/pest2.jpeg"]
    },
    {
        "id": 3,
        "slug": "trusted-and-reliable-professionals",
        "title": "Trusted and Reliable Professionals",
        "description": "Rest assured that the affiliated employee assigned to your organization undergoes a rigorous selection process, including thorough background checks and comprehensive training. They are committed to maintaining the highest standards of professionalism, integrity, and confidentiality.",
        "images": ["/static/assets/images/training.jpeg", "/static/assets/images/laundry1.jpeg", "/static/assets/images/laundry2.jpeg"]
    },
    {
        "id": 4,
        "slug": "enhanced-communication",
        "title": "Enhanced Communication",
        "description": "Clear and open lines of communication are essential for a successful affiliation. We foster strong communication channels between you, your dedicated employee, and our support team to ensure that any questions, concerns, or adjustments are promptly addressed.",
        "images": ["/static/assets/images/training.jpeg", "/static/assets/images/bathroom1.jpeg", "/static/assets/images/bathroom2.jpeg"]
    },
    {
        "id": 5,
        "slug": "consistency-and-contiunity",
        "title": "Consistency and Continuity",
        "description": "With an affiliated employee, you can enjoy consistent and uninterrupted cleaning services. They will be well-versed in your specific cleaning routines, allowing for seamless transitions and avoiding disruptions during employee absences or turnover.",
        "images": ["/static/assets/images/training.jpeg", "/static/assets/images/rug1.jpeg", "/static/assets/images/rug2.jpeg"]
    },

]


class LandingPageView(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        self.context = {
        'services': services,
        'trainings': trainings
        }
        return render(request, self.template_name, self.context)
    

class AboutPageView(View):
    template_name = "about.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    


class ContactPageView(View):
    template_name = "contact.html"

    def get(self, request):

        return render(request, self.template_name)


class ServicePageView(View):
    template_name = "services.html"
    context = {
        'services': services
    }

    def get(self, request):
        return render(request, self.template_name, self.context)
    

class ServiceDetailPageView(View):
    template_name = "service_detail.html"
    context = {}

    def get(self, request, service_slug):
        # service = None
        for s in services:
            if s["slug"] == service_slug:
                self.context.update(s)
                break

        return render(request, self.template_name, self.context)


class TrainingPageView(View):
    template_name = "training.html"
    context = {}

    def get(self, request):
        self.context = {
            'trainings': trainings
        }
        
        return render(request, self.template_name, self.context)


class TrainingDetailPageView(View):
    template_name = "training_detail.html"
    context = {}

    def get(self, request, training_slug):
        # service = None
        for s in trainings:
            if s["slug"] == training_slug:
                self.context.update(s)
                break

        return render(request, self.template_name, self.context)
    
