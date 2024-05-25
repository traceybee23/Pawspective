from app.models import db, Business, environment, SCHEMA
from sqlalchemy.sql import text

def seed_businesses_4():
    businesses_4 = [
      Business(
        owner_id=12,
        category_id=1,
        address='6080 Falls Rd',
        city='Baltimore',
        state='MD',
        zip_code='21212',
        name='The Corner Pantry',
        description='The Corner Pantry is a casual eatery offering British-American cuisine. The outdoor seating area is dog-friendly, so you can enjoy a meal with your furry friend.',
        website='https://www.corner-pantry.com/',
        email='info@corner-pantry.com',
        phone='6673082331',
        price='$$',
        set_hours='yes',
        mon_open='0700',
        mon_close='1500',
        tue_open='0700',
        tue_close='1500',
        wed_open='0700',
        wed_close='1500',
        thu_open='0700',
        thu_close='1500',
        fri_open='0700',
        fri_close='1500',
        sat_open='0800',
        sat_close='1500',
      ),
      Business(
        owner_id=23,
        category_id=2,
        address='716 York Rd',
        city='Towson',
        state='MD',
        zip_code='21204',
        name='Towson Veterinary Hospital',
        description='Towson Veterinary Hospital offers comprehensive veterinary care including exams, surgery, dental treatment, and ultrasound diagnostics. They also provide boarding services for pets.',
        website='https://www.towsonveterinary.com',
        email='reception@towson.vet',
        phone='4108258880',
        price='$$',
        set_hours='yes',
        mon_open='0900',
        mon_close='1800',
        tue_open='0900',
        tue_close='1800',
        wed_open='0900',
        wed_close='1800',
        thu_open='0900',
        thu_close='1800',
        fri_open='0900',
        fri_close='1800',
        sat_open='0900',
        sat_close='1800',
      ),
      Business(
        owner_id=17,
        category_id=3,
        address='240 Town Square Dr',
        city='Lusby',
        state='MD',
        zip_code='20657',
        name='Bark & Bath Pet Salon',
        description='Bark & Bath Pet Salon is a friendly, high end pet grooming facility located in Lusby, Maryland. Our salon accommodates cats and dogs of all breeds! We take pride in maintaining a clean and stress free salon environment.',
        website='http://www.barkandbathpetsalon.com/',
        email='barkandbathpetsalon@yahoo.com',
        phone='4102312527',
        set_hours='yes',
        mon_open='0800',
        mon_close='1600',
        tue_open='0800',
        tue_close='1600',
        wed_open='0800',
        wed_close='1600',
        thu_open='0800',
        thu_close='1600',
        fri_open='0800',
        fri_close='1600',
        sat_open='0800',
        sat_close='1200',
      ),
      Business(
        owner_id=5,
        category_id=4,
        address='3531 Chestnut Avenue',
        city='Baltimore',
        state='MD',
        zip_code='21211',
        name='Howl',
        description='Howl offers a variety of pet products including food, toys, and accessories. They also offer pet grooming services.',
        website='https://www.howlinhampden.com/',
        email='howlinhampden@gmail.com',
        phone='4102352469',
        price='$$',
        set_hours='yes',
        mon_open='1100',
        mon_close='1900',
        tue_open='1100',
        tue_close='1900',
        wed_open='1100',
        wed_close='1900',
        thu_open='1100',
        thu_close='1900',
        fri_open='1100',
        fri_close='1900',
        sat_open='1100',
        sat_close='1700',
        sun_open='1100',
        sun_close='1700',
      ),
      Business(
        owner_id=28,
        category_id=5,
        address='1734 W Nursery Rd',
        city='Linthicum Heights',
        state='MD',
        zip_code='21090',
        name='La Quinta Inn & Suites by Wyndham Baltimore BWI Airport',
        description='This pet-friendly hotel near BWI Airport offers comfortable accommodations for travelers and their pets, with easy access to Baltimore attractions.',
        website='https://www.wyndhamhotels.com/laquinta/linthicum-maryland/la-quinta-baltimore-bwi-airport/overview?CID=LC:6ysy27krtpcrqev:52918&iata=00093796',
        phone='4108592333',
        price='$$$',
        set_hours='no',
      ),
      Business(
        owner_id=3,
        category_id=6,
        address='1000 Lakeside Dr',
        city='Baltimore',
        state='MD',
        zip_code='21210',
        name='Lake Roland Park',
        description='Lake Roland Park offers scenic trails and open spaces that are perfect for outdoor activities with your dog. The park includes a designated dog park and swim area known as Paw Point Dog Park.',
        website='https://www.lakeroland.org',
        email='lakerol-rp@baltimorecountymd.gov',
        phone='4108874156',
        set_hours='no',
        mon_open='0600',
        mon_close='2200',
        tue_open='0600',
        tue_close='2200',
        wed_open='0600',
        wed_close='2200',
        thu_open='0600',
        thu_close='2200',
        fri_open='0600',
        fri_close='2200',
        sat_open='0600',
        sat_close='2200',
        sun_open='0600',
        sun_close='2200',
      ),
      Business(
        owner_id=8,
        category_id=7,
        address='3300 Falls Rd',
        city='Baltimore',
        state='MD',
        zip_code='21211',
        name='Maryland SPCA',
        description='Maryland SPCA is dedicated to improving the lives of pets and people by providing adoption services, veterinary care, and community programs.',
        website='https://www.mdspca.org',
        phone='4102358826',
        price='$$',
        set_hours='yes',
        mon_open='1300',
        mon_close='1900',
        tue_open='1300',
        tue_close='1900',
        wed_open='1300',
        wed_close='1900',
        thu_open='1300',
        thu_close='1900',
        fri_open='1300',
        fri_close='1900',
        sat_open='1200',
        sat_close='1700',
      ),
      Business(
        owner_id=21,
        category_id=8,
        address='3500 Parkdale Ave Fl 2 Ste R',
        city='Baltimore',
        state='MD',
        zip_code='21211',
        name='Puptrait',
        description='Puptrait is an award winning dog-friendly photography studio located in the heart of Baltimore City, Maryland. We are world renowned for our anthropomorphic pet portraits and original handmade costume designs.',
        website='https://puptrait.com/',
        email='help@puptrait.com',
        phone='4436040711',
        price='$$$',
        set_hours='no',
        mon_open='1200',
        mon_close='2200',
        tue_open='1200',
        tue_close='2200',
        wed_open='1200',
        wed_close='2200',
        thu_open='1200',
        thu_close='2200',
        fri_open='1200',
        fri_close='2200',
        sat_open='1200',
        sat_close='2200',
        sun_open='1200',
        sun_close='2200',
      ),
      Business(
        owner_id=30,
        category_id=1,
        address='3307 N Davidson St',
        city='Charlotte',
        state='NC',
        zip_code='28205',
        name='The Dog Bar',
        description='The Dog Bar in Charlotte, NC is THE pet-friendly place to bring Fido in the Queen City. Located in the NoDa Arts District, the bar serves beer, wine, and liquor, and allows dogs of all shapes and sizes both indoors and out.',
        website='https://www.dogbarcharlotte.net/',
        email='office@dogbarcharlotte.net',
        phone='7043703595',
        price='$',
        set_hours="yes",
        tue_open='1700',
        tue_close='2200',
        wed_open='1700',
        wed_close='2200',
        thu_open='1700',
        thu_close='2200',
        fri_open='1700',
        fri_close='2200',
        sat_open='1200',
        sat_close='2200',
        sun_open='1200',
        sun_close='2200',
      ),
      Business(
        owner_id=24,
        category_id=2,
        address='9729 S Tryon St',
        city='Charlotte',
        state='NC',
        zip_code='28273',
        name='Steele Creek Animal Hospital',
        description='At Steele Creek Animal Hospital in Charlotte, NC, we offer a wide-range of services to help your animal in any way we can. Call us today!',
        website='https://www.keepingpetshealthy.com/',
        phone='7045884400',
        set_hours="yes",
        mon_open='0700',
        mon_close='1800',
        tue_open='0700',
        tue_close='1800',
        wed_open='0700',
        wed_close='1800',
        thu_open='0700',
        thu_close='1800',
        fri_open='0700',
        fri_close='1800',
        sat_open='0700',
        sat_close='1200',
      ),
      Business(
        owner_id=15,
        category_id=3,
        address='5011 Weddington Rd NW Suite 60',
        city='Concord',
        state='NC',
        zip_code='28027',
        name='Woof Gang Bakery & Grooming',
        description='Woof Gang Bakery & Grooming is the leader in professional pet grooming, and the leading specialty retailer of pet food and supplies in the country. Our pet grooming services, butt scratches, and nose boops are the best in the industry!',
        website='https://woofgangbakery.com/',
        phone='9802558116',
        email='concordnc@woofgangbakery.com',
        set_hours="yes",
        mon_open='1000',
        mon_close='1800',
        tue_open='1000',
        tue_close='1800',
        wed_open='1000',
        wed_close='1800',
        thu_open='1000',
        thu_close='1800',
        fri_open='1000',
        fri_close='1800',
        sat_open='1000',
        sat_close='1800',
        sun_open='1200',
        sun_close='1800',
      ),
      Business(
        owner_id=29,
        category_id=4,
        address='4110 Charlotte Hwy',
        city='Lake Wylie',
        state='SC',
        zip_code='28209',
        name='Pet Wants Lake Wylie',
        description='Lake Wylie, SC\'s Pet Wants is a specialty shop that focuses on pet nutrition and educating pet parents on the importance of healthy food for your dog. Fresh, simple ingredients make up their food that\'s made fresh every 45 days.',
        website='https://www.petwantslakewylie.com/',
        phone='8036101228',
        email='kbyrd@petwants.com',
        set_hours="yes",
        tue_open='1000',
        tue_close='1800',
        wed_open='1000',
        wed_close='1800',
        thu_open='1000',
        thu_close='1800',
        fri_open='1000',
        fri_close='1800',
        sat_open='1000',
        sat_close='1800',
        sun_open='1200',
        sun_close='1700',
        ),
      Business(
        owner_id=26,
        category_id=5,
        address='222 East 3rd St',
        city='Charlotte',
        state='NC',
        zip_code='28202',
        name='Aloft Charlotte City Center',
        description='Aloft Charlotte City Center welcomes both dogs and cats, and well-behaved pets may be left in the room unattended. Treats, beds, and food and water bowls are available at the front desk. ',
        website='https://www.marriott.com/en-us/hotels/cltul-aloft-charlotte-city-center/overview/?scid=f2ae0541-1279-4f24-b197-a979c79310b0',
        phone='7043331999',
        price='$$$',
        set_hours="no",
      ),
      Business(
        owner_id=20,
        category_id=6,
        address='15222 York Rd',
        city='Charlotte',
        state='NC',
        zip_code='28278',
        name='McDowell Nature Preserve',
        description='McDowell Nature Preserve offers scenic trails, fishing, and camping. Dogs are welcome on the trails and in the camping areas.',
        website='https://parkandrec.mecknc.gov/Places-to-Visit/Nature/mcdowell-nature-center-and-preserve',
        email='mdnp@MeckNC.gov',
        phone='9803141128',
        set_hours="yes",
        mon_open='0900',
        mon_close='1700',
        tue_open='0900',
        tue_close='1700',
        wed_open='0900',
        wed_close='1700',
        thu_open='0900',
        thu_close='1700',
        fri_open='0900',
        fri_close='1700',
        sat_open='0900',
        sat_close='1700',
        sun_open='1300',
        sun_close='1700',
      ),
      Business(
        owner_id=10,
        category_id=7,
        address='1348 Parker Dr',
        city='Charlotte',
        state='NC',
        zip_code='28208',
        name='The Humane Society of Charlotte',
        description='The Humane Society of Charlotte offers pet adoption services and community education programs. They aim to improve the lives of pets and people through compassion and care.',
        website='https://www.humanesocietyofcharlotte.org',
        phone='7043770534',
        set_hours="yes",
        mon_open='1100',
        mon_close='1700',
        tue_open='1100',
        tue_close='1700',
        wed_open='1100',
        wed_close='1700',
        thu_open='1100',
        thu_close='1700',
        fri_open='1100',
        fri_close='1900',
        sat_open='1100',
        sat_close='1800',
        sun_open='1100',
        sun_close='1700',
      ),
      Business(
        owner_id=25,
        category_id=8,
        address='8431 Old Statesville Rd',
        city='Charlotte',
        state='NC',
        zip_code='28203',
        name='DoodyCalls',
        description='DoodyCalls provides dog pooper scooper service for your yard, patio/deck deodorizing, as well as pet dog waste station set up and maintenance for communities.',
        website='https://www.doodycalls.com/charlotte/',
        phone='7046100545',
        email='charlottedoodycalls@live.com',
        set_hours="yes",
        mon_open='0830',
        mon_close='2100',
        tue_open='0830',
        tue_close='2100',
        wed_open='0830',
        wed_close='2100',
        thu_open='0830',
        thu_close='2100',
        fri_open='0830',
        fri_close='2100',
        sat_open='0900',
        sat_close='1700',
        sun_open='1230',
        sun_close='1530',
      ),
      Business(
        owner_id=23,
        category_id=1,
        address=' 6400 Time Square Ave',
        city='Orlando',
        state='FL',
        zip_code='32835',
        name='Teak Neighborhood Grill',
        description='Casual eatery with a pet-friendly patio serving microbrews & handcrafted burgers, this pub with a patio hosts trivia nights & live music.',
        website='https://teakorlando.com/',
        email='teakorlando@live.com',
        phone='4073135111',
        price='$$',
        set_hours="yes",
        mon_open='1130',
        mon_close='2300',
        tue_open='1130',
        tue_close='2300',
        wed_open='1130',
        wed_close='2300',
        thu_open='1130',
        thu_close='2300',
        fri_open='1100',
        fri_close='2400',
        sat_open='1100',
        sat_close='2400',
        sun_open='1100',
        sun_close='2300',
    ),
      Business(
        owner_id=11,
        category_id=2,
        address='1201 W Michigan St',
        city='Orlando',
        state='FL',
        zip_code='32805',
        name='Michigan Street Animal Hospital',
        description='Full-service veterinary hospital offering comprehensive medical, surgical, and dental care.',
        website='https://www.michiganstreetvet.com/',
        email= 'westmichiganstvet@gmail.com',
        phone='3177575077',
        set_hours="yes",
        mon_open='0800',
        mon_close='1700',
        tue_open='0800',
        tue_close='1700',
        wed_open='0800',
        wed_close='1700',
        thu_open='0800',
        thu_close='1700',
        fri_open='0800',
        fri_close='1700',
        sat_open='0800',
        sat_close='1200',
      ),
      Business(
        owner_id=4,
        category_id=3,
        address='3815 Lake Center Dr',
        city='MT Dora',
        state='FL',
        zip_code='32757',
        name='The Green K9',
        description='Professional dog grooming and boarding services with a focus on natural pet care.',
        website='https://thegreenk9.com/',
        email='info@thegreenk9.com',
        phone='3527296172',
        set_hours="yes",
        mon_open='0730',
        mon_close='1800',
        tue_open='0730',
        tue_close='1800',
        wed_open='0730',
        wed_close='1800',
        thu_open='0730',
        thu_close='1800',
        fri_open='0730',
        fri_close='1800',
        sat_open='1000',
        sat_close='1600',
        sun_open='1000',
        sun_close='1600',
      ),
      Business(
        owner_id=19,
        category_id=4,
        address='460 N Ronald Reagan Blvd',
        city='Longwood',
        state='FL',
        zip_code='32750',
        name='Doggo Lovers',
        description='Doggo Lovers in Longwood, FL, is a pet supply store and dog boutique. They carry dog food, treats, pet care items, bowls, leashes, jewelry and accessories',
        website='https://doggolovers.com/',
        email='doggoloversfl@gmail.com',
        phone='6892479993',
        set_hours="yes",
        mon_open='1000',
        mon_close='1900',
        tue_open='1000',
        tue_close='1900',
        wed_open='1000',
        wed_close='1900',
        thu_open='1000',
        thu_close='1900',
        fri_open='1000',
        fri_close='1900',
        sat_open='1000',
        sat_close='1700',
      ),
      Business(
        owner_id=13,
        category_id=5,
        address='8480 International Dr',
        city='Orlando',
        state='FL',
        zip_code='32819',
        name='Sonesta ES Suites Orlando - International Drive',
        description='Sonesta ES Suites Orlando - International Drive welcomes two dogs of any size for an additional fee of $75 (for stays of 1 to 7 nights), and $25 per week thereafter. Cats are not allowed.',
        website='https://www.sonesta.com/sonesta-es-suites/fl/orlando/sonesta-es-suites-orlando-international-drive',
        phone='4073522400',
        price='$$',
        set_hours="no",
      ),
      Business(
        owner_id=7,
        category_id=6,
        address='512 East Washington St',
        city='Orlando',
        state='FL',
        zip_code='32801',
        name='Lake Eola Park',
        description='Beautiful park in downtown Orlando, offering walking trails, swan boat rentals, and a large lake. Dogs are welcome on leashes.',
        website='https://www.cityoforlando.net/parks/lake-eola-park/',
        phone='4072464484',
        set_hours="yes",
        mon_open='0600',
        mon_close='2359',
        tue_open='0600',
        tue_close='2359',
        wed_open='0600',
        wed_close='2359',
        thu_open='0600',
        thu_close='2359',
        fri_open='0600',
        fri_close='2359',
        sat_open='0600',
        sat_close='2359',
        sun_open='0600',
        sun_close='2359',
      ),
      Business(
        owner_id=28,
        category_id=7,
        address='2769 Conroy Rd',
        city='Orlando',
        state='FL',
        zip_code='32839',
        name='Orange County Animal Services',
        description='Animal shelter providing pet adoption services, community education, and veterinary care.',
        website='https://www.ocnetpets.com/',
        phone='4078363111',
        set_hours="yes",
        mon_open='1000',
        mon_close='1800',
        tue_open='1000',
        tue_close='1800',
        wed_open='1400',
        wed_close='1800',
        thu_open='1000',
        thu_close='1800',
        fri_open='1000',
        fri_close='1800',
        sat_open='1000',
        sat_close='1800',
        sun_open='1000',
        sun_close='1800',
      ),
      Business(
        owner_id=16,
        category_id=8,
        address='7284 Narcoossee Rd',
        city='Orlando',
        state='FL',
        zip_code='32822',
        name='Orlando Pet Crematory',
        description='Specializing in helping families create unforgettable memorials of beautiful moments shared with pets.',
        website='https://orlandopetcrematory.com/',
        phone='4073817474',
        set_hours="yes",
        mon_open='0900',
        mon_close='1530',
        tue_open='0900',
        tue_close='1530',
        wed_open='0900',
        wed_close='1530',
        thu_open='0900',
        thu_close='1530',
        fri_open='0900',
        fri_close='1530',
      ),
      Business(
        owner_id=5,
        category_id=1,
        address='245 E Commerce St Ste 100',
        city='San Antonio',
        state='TX',
        zip_code='78205',
        name='Rita\'s on the River',
        description='Mexican restaurant on the Riverwalk where you can dine with your pup. While you sip on a margarita, your dog can have something from the dog menu that includes dog-friendly ice cream, white rice with zucchini and carrots, and a free dog water slushy.',
        website='https://ritasontheriver.com/',
        phone='2102277482',
        price='$$',
        set_hours="yes",
        mon_open='1100',
        mon_close='2200',
        tue_open='1100',
        tue_close='2200',
        wed_open='1100',
        wed_close='2200',
        thu_open='1100',
        thu_close='2200',
        fri_open='1100',
        fri_close='2300',
        sat_open='1100',
        sat_close='2300',
      ),
      Business(
        owner_id=12,
        category_id=2,
        address='6820 Alamo Pkwy STE 118',
        city='San Antonio',
        state='TX',
        zip_code='78253',
        name='Alamo Ranch Animal Hospital',
        description='Full-service veterinary hospital offering comprehensive pet care.',
        website='https://alamoranchvets.com/',
        phone='2105387484',
        set_hours="yes",
        mon_open='0730',
        mon_close='1730',
        tue_open='0730',
        tue_close='1730',
        wed_open='0730',
        wed_close='1730',
        thu_open='0730',
        thu_close='1730',
        fri_open='0730',
        fri_close='1730',
      ),
      Business(
        owner_id=18,
        category_id=3,
        address='5010 N Loop 1604 W',
        city='San Antonio',
        state='TX',
        zip_code='78249',
        name='Lucy\'s Doggy Daycare and Spa',
        description='Offering dog daycare, boarding, grooming, and spa services.',
        website='https://www.lucysdoggydaycare.com/',
        email='info@lucysdoggydaycare.com',
        phone='2104953647',
        set_hours="yes",
        mon_open='0700',
        mon_close='2000',
        tue_open='0700',
        tue_close='2000',
        wed_open='0700',
        wed_close='2000',
        thu_open='0700',
        thu_close='2000',
        fri_open='0700',
        fri_close='2000',
        sat_open='0800',
        sat_close='1800',
        sun_open='0800',
        sun_close='1600',
      ),
      Business(
        owner_id=25,
        category_id=4,
        address='5120 Broadway St',
        city='San Antonio',
        state='TX',
        zip_code='78209',
        name='Fifi & Fidos Pet Boutique',
        description='Upscale boutique carrying food & treats for dogs & cats, also offers pet nutrition advice.',
        website='https://fifiandfidos.com/',
        phone='2108222525',
        set_hours="yes",
        mon_open='1000',
        mon_close='1800',
        tue_open='1000',
        tue_close='1800',
        wed_open='1000',
        wed_close='1800',
        thu_open='1000',
        thu_close='1800',
        fri_open='1000',
        fri_close='1800',
        sat_open='1000',
        sat_close='1800',
      ),
      Business(
        owner_id=7,
        category_id=5,
        address='420 W Market St',
        city='San Antonio',
        state='TX',
        zip_code='78205',
        name='The Westin Riverwalk, San Antonio',
        description='Pet-friendly hotel offering upscale accommodations along the Riverwalk.',
        website='https://www.marriott.com/en-us/hotels/satvw-the-westin-riverwalk-san-antonio/overview/',
        phone='2102246500',
        price='$$$',
        set_hours="no",
      ),
      Business(
        owner_id=20,
        category_id=6,
        address='13203 Blanco Rd',
        city='San Antonio',
        state='TX',
        zip_code='78216',
        name='Phil Hardberger Park',
        description='A large park with trails, dog parks, and picnic areas.',
        website='https://www.philhardbergerpark.org/',
        phone='2104927472',
        set_hours='no'
      ),
      Business(
        owner_id=14,
        category_id=7,
        address='4804 Fredericksburg Rd',
        city='San Antonio',
        state='TX',
        zip_code='78229',
        name='San Antonio Humane Society',
        description='Animal shelter offering pet adoption services.',
        website='https://sahumane.org/',
        email='communication@sahumane.org',
        phone='2102267461',
        set_hours="yes",
        mon_open='1200',
        mon_close='1900',
        tue_open='1200',
        tue_close='1900',
        wed_open='1200',
        wed_close='1900',
        thu_open='1200',
        thu_close='1900',
        fri_open='1200',
        fri_close='1900',
        sat_open='1200',
        sat_close='1900',
        sun_open='1200',
        sun_close='1900',
      ),
      Business(
        owner_id=27,
        category_id=8,
        address='5611 E. Houston St.',
        city='San Antonio',
        state='TX',
        zip_code='78220',
        name='All Paws Great & Small Pet Funeral Home & Crematory',
        description='Providing pet burial and cremation services in a respectful manner.',
        website='https://www.faithfulfriendscrematory.com/',
        phone='2106617297',
        set_hours="yes",
        mon_open='0800',
        mon_close='1700',
        tue_open='0800',
        tue_close='1700',
        wed_open='0800',
        wed_close='1700',
        thu_open='0800',
        thu_close='1700',
        fri_open='0800',
        fri_close='1700',
        sat_open='0800',
        sat_close='1400',
      ),
      Business(
        owner_id=48,
        category_id=3,
        address=' 7182 Oak Dr.',
        city='San Antonio',
        state='TX',
        zip_code='78256',
        name='Barkaritaville Pet Resort',
        description='Barkaritaville Pet Resort is a full-service, state of the art pet resort in San Antonio, TX, with luxury lodging, doggie daycare, grooming salon and spa, dog training, DIY dog wash, and more!',
        website='https://www.faithfulfriendscrematory.com/',
        email='infosa@barkpr.us',
        phone='2104052275',
        set_hours="yes",
        mon_open='0700',
        mon_close='1800',
        tue_open='0700',
        tue_close='1800',
        wed_open='0700',
        wed_close='1800',
        thu_open='0700',
        thu_close='1800',
        fri_open='0700',
        fri_close='1800',
        sat_open='0800',
        sat_close='1700',
      )
    ]

    db.session.add_all(businesses_4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_businesses_4():
    if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.businesses RESTART IDENTITY CASCADE;")
    else:
      db.session.execute(text("DELETE FROM businesses"))
    db.session.commit()
