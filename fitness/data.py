"""
Static demo data for the frontend-only fitness website.
This is NOT a database — just plain Python structures passed
into templates as context so pages aren't hardcoded with
repeated markup. Fully allowed since the project explicitly
avoids Django models / DB, not Python variables.
"""

WORKOUT_CATEGORIES = [
    {"name": "Chest", "icon": "fa-shield-heart", "count": 24,
    "url": "chest-exercises",
     "img": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D=format&fit=crop"},
    {"name": "Back", "icon": "fa-shield-halved", "count": 20,
     "url": "back-exercises",
     "img": "https://images.unsplash.com/photo-1606755612718-95150ca71a0c?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D=format&fit=crop"},
    {"name": "Legs", "icon": "fa-person-walking", "count": 20,
     "url": "legs-exercises",
     "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800&auto=format&fit=crop"},
    {"name": "Shoulders", "icon": "fa-child-reaching", "count": 16,
     "url": "shoulders-exercises",
     "img": "https://images.unsplash.com/photo-1620188467120-5042ed1eb5da?q=80&w=800&auto=format&fit=crop"},
    {"name": "Arms", "icon": "fa-hand-fist", "count": 20,
     "url": "arms-exercises",
     "img": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=800&auto=format&fit=crop"},
    {"name": "Core", "icon": "fa-bolt", "count": 18,
     "url": "core-exercises",
     "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=800&auto=format&fit=crop"},
    {"name": "Cardio", "icon": "fa-heart-pulse", "count": 14,
     "url": "cardio-exercises",
     "img": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=800&auto=format&fit=crop"},
    {"name": "Full Body", "icon": "fa-dumbbell", "count": 20,
     "url": "full-body-exercises",
     "img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=800&auto=format&fit=crop"},
]

WORKOUT_PLANS = [
    {"name": "Iron Beginner Foundations", "level": "Beginner", "duration": "4 Weeks", "calories": "300-400 kcal",
     "days": "3 Days/wk", "desc": "Build core strength & movement patterns before progressing to heavier lifts.",
     "img": "https://images.unsplash.com/photo-1571731956672-f2b94d7dd0cb?q=80&w=800&auto=format&fit=crop"},
    {"name": "Hypertrophy Mass Builder", "level": "Intermediate", "duration": "8 Weeks", "calories": "450-550 kcal",
     "days": "5 Days/wk", "desc": "A push/pull/legs split designed for maximum muscle growth.",
     "img": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=800&auto=format&fit=crop"},
    {"name": "Elite Strength & Power", "level": "Advanced", "duration": "12 Weeks", "calories": "500-650 kcal",
     "days": "6 Days/wk", "desc": "Heavy compound lifts and periodized programming for elite performance.",
     "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800&auto=format&fit=crop"},
    {"name": "Fat Shred HIIT Circuit", "level": "Intermediate", "duration": "6 Weeks", "calories": "550-700 kcal",
     "days": "4 Days/wk", "desc": "High-intensity interval circuits designed to torch calories fast.",
     "img": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=800&auto=format&fit=crop"},
    {"name": "Functional Athlete Program", "level": "Advanced", "duration": "10 Weeks", "calories": "480-600 kcal",
     "days": "5 Days/wk", "desc": "Sport-focused training for agility, explosiveness and endurance.",
     "img": "https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?q=80&w=800&auto=format&fit=crop"},
    {"name": "Home Bodyweight Blast", "level": "Beginner", "duration": "4 Weeks", "calories": "250-350 kcal",
     "days": "3 Days/wk", "desc": "No-equipment full body routine you can do anywhere, anytime.",
     "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=800&auto=format&fit=crop"},
]

DIET_PLANS = [
    {"name": "Lean Cut Meal Plan", "desc": "High protein, moderate carb plan built for sustainable fat loss.",
     "kcal": "1800 kcal/day", "goal": "Weight Loss",
     "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format&fit=crop"},
    {"name": "Mass Gainer Nutrition", "desc": "Calorie-dense whole food plan to fuel serious muscle growth.",
     "kcal": "3200 kcal/day", "goal": "Muscle Gain",
     "img": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800&auto=format&fit=crop"},
    {"name": "Balanced Maintenance Plan", "desc": "Well-rounded macros to sustain performance and energy.",
     "kcal": "2400 kcal/day", "goal": "Maintenance",
     "img": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?q=80&w=800&auto=format&fit=crop"},
    {"name": "Plant-Powered Athlete", "desc": "100% plant-based nutrition plan for endurance & recovery.",
     "kcal": "2200 kcal/day", "goal": "Vegan",
     "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format&fit=crop"},
    {"name": "Keto Shred Protocol", "desc": "Low-carb, high-fat plan for rapid fat adaptation and loss.",
     "kcal": "1900 kcal/day", "goal": "Weight Loss",
     "img": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?q=80&w=800&auto=format&fit=crop"},
    {"name": "Competition Prep Diet", "desc": "Precision macro cycling for stage-ready conditioning.",
     "kcal": "Varies (cycled)", "goal": "Contest Prep",
     "img": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800&auto=format&fit=crop"},
]

TRAINERS = [
    {"name": "Marcus Reed", "role": "Head Strength Coach", "bio": "12+ years training competitive powerlifters and everyday athletes alike.",
     "img": "https://images.unsplash.com/photo-1567013127542-490d757e51fc?q=80&w=800&auto=format&fit=crop"},
    {"name": "Sofia Cruz", "role": "HIIT & Conditioning", "bio": "Former national sprinter specializing in fat-loss conditioning programs.",
     "img": "https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=800&auto=format&fit=crop"},
    {"name": "Daniel Okafor", "role": "Bodybuilding Coach", "bio": "IFBB-certified coach focused on hypertrophy and physique competitions.",
     "img": "https://images.unsplash.com/photo-1546484959-f9a381d1330d?q=80&w=800&auto=format&fit=crop"},
    {"name": "Elena Petrova", "role": "Nutrition & Wellness", "bio": "Registered dietitian pairing training plans with science-based nutrition.",
     "img": "https://images.unsplash.com/photo-1594381898411-846e7d193883?q=80&w=800&auto=format&fit=crop"},
    {"name": "Jason Lee", "role": "Functional Training", "bio": "Specializes in mobility, injury prevention, and athletic performance.",
     "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=800&auto=format&fit=crop"},
    {"name": "Amara Johnson", "role": "Yoga & Recovery", "bio": "Helps members build flexibility, balance, and mind-muscle connection.",
     "img": "https://images.unsplash.com/photo-1548690312-e3b507d8c110?q=80&w=800&auto=format&fit=crop"},
]

TRANSFORMATION_IMAGES = [
    "https://images.unsplash.com/photo-1571731956672-f2b94d7dd0cb?q=80&w=800&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=800&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?q=80&w=800&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800&auto=format&fit=crop",
]

GALLERY_IMAGES = [
    {"img": "https://bizweb.dktcdn.net/100/011/344/files/nguoi-gay-co-nen-tap-gym-khong-4.jpg?v=1651551552587", "cat": "transformation"},
    {"img": "https://miro.medium.com/0%2AXMPGvm0Xs1c1DRqO", "cat": "transformation"},
    {"img": "https://ironbuiltfitness.com/wp-content/uploads/2019/01/skinny-fat-to-ripped-2-700x632.jpg", "cat": "transformation"},
    {"img": "https://cdn.shopify.com/s/files/1/2137/7825/files/ChrisB_A_bd8a6725-24a1-40ea-a6d6-229872539e59.png?v=1722351118", "cat": "transformation"},
    {"img": "https://justinhealth.com/wp-content/uploads/2024/09/Point-5-588x600.jpeg", "cat": "transformation"},
    {"img": "https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https%3A/assets.cdn.filesafe.space/0foQJGs9QbPwvouJwzlx/media/67c9b83f0eb02a76b8bf83db.png", "cat": "transformation"},
    {"img": "https://pbs.twimg.com/media/DDuiCe3XcAA0uVo.jpg", "cat": "transformation"},
    {"img": "https://i.pinimg.com/736x/44/6a/03/446a03ec29d9c73130770c6d225f7829.jpg", "cat": "transformation"},
    {"img": "https://seyler.ekstat.com/img/max/800/f/fa86TzawF13Owsfa-636566369587517997.jpg", "cat": "transformation"},
    {"img": "https://i.pinimg.com/736x/9f/3f/c1/9f3fc1cfec998ef3c5fce5413fcedac9.jpg", "cat": "transformation"},
    {"img": "https://forum.science-fitness.de/uploads/monthly_2020_02/PicsArt_02-11-11_17_32.jpg.04016575077d3a233bf3fc4446641b95.jpg", "cat": "transformation"},
    {"img": "https://static.wixstatic.com/media/aeaaf1_e76c60cdf0de4ac1b3b98e2cab463afc~mv2.png/v1/fill/w_568%2Ch_568%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/aeaaf1_e76c60cdf0de4ac1b3b98e2cab463afc~mv2.png", "cat": "transformation"},
]

PRICING_PLANS = [
    {"id": 1, "tag": "Basic", "price": 1499, "featured": False, "desc": "Perfect for getting started with your fitness journey.",
     "features": ["Full Gym Access", "2 Group Classes/mo", "Locker Room Access", "Mobile App Access"]},
    {"id": 2, "tag": "Pro", "price": 2999, "featured": True, "desc": "Our most popular plan for serious, consistent training.",
     "features": ["Full Gym Access", "Unlimited Group Classes", "1 PT Session/mo", "Diet Plan Included", "Sauna & Recovery Zone"]},
    {"id": 3, "tag": "Elite", "price": 4999, "featured": False, "desc": "All-access pass with dedicated personal coaching.",
     "features": ["Full Gym Access", "Unlimited Group Classes", "8 PT Sessions/mo", "Custom Diet & Program", "Priority Booking", "Guest Passes x2"]},
]

TESTIMONIALS = [
    {"name": "Ryan Cooper", "role": "Member since 2022", "quote": "IRONCORE completely changed how I train. Down 18kg and stronger than ever.",
     "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=200&auto=format&fit=crop"},
    {"name": "Maria Gonzalez", "role": "Member since 2023", "quote": "The trainers actually care. My squat has doubled in eight months.",
     "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=200&auto=format&fit=crop"},
    {"name": "Tom Becker", "role": "Member since 2021", "quote": "Best gym atmosphere I've trained in. Clean, modern, motivating.",
     "img": "https://images.unsplash.com/photo-1607990281513-2c110a25bd8c?q=80&w=200&auto=format&fit=crop"},
    {"name": "Priya Nair", "role": "Member since 2024", "quote": "The diet plans made all the difference — finally hit my goal weight.",
     "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=200&auto=format&fit=crop"},
    {"name": "Chris Walker", "role": "Member since 2020", "quote": "Four years here and I still look forward to every session.",
     "img": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=200&auto=format&fit=crop"},
    {"name": "Nadia Farouk", "role": "Member since 2023", "quote": "Supportive community, great equipment, real results.",
     "img": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?q=80&w=200&auto=format&fit=crop"},
]

BLOG_POSTS = [
    {"title": "5 Compound Lifts Every Beginner Should Master", "category": "training",
     "excerpt": "Build a rock-solid foundation with these five essential movements before chasing isolation work.",
     "date": "July 10, 2026", "author": "Marcus Reed", "read_time": "6 min read",
     "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800&auto=format&fit=crop"},
    {"title": "How Much Protein Do You Actually Need?", "category": "nutrition",
     "excerpt": "We break down the science behind protein intake for muscle growth and recovery.",
     "date": "July 2, 2026", "author": "Elena Petrova", "read_time": "5 min read",
     "img": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800&auto=format&fit=crop"},
    {"title": "The Truth About Fat-Burning Cardio Zones", "category": "cardio",
     "excerpt": "Is low-intensity steady state really better for fat loss? Here's what the research says.",
     "date": "June 24, 2026", "author": "Sofia Cruz", "read_time": "4 min read",
     "img": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=800&auto=format&fit=crop"},
    {"title": "Recovery 101: Sleep, Stretching & Rest Days", "category": "recovery",
     "excerpt": "Why your gains happen outside the gym — and how to optimize your recovery routine.",
     "date": "June 15, 2026", "author": "Amara Johnson", "read_time": "7 min read",
     "img": "https://images.unsplash.com/photo-1548690312-e3b507d8c110?q=80&w=800&auto=format&fit=crop"},
    {"title": "Building Mental Toughness for Heavy Lifts", "category": "mindset",
     "excerpt": "Mindset techniques used by elite lifters to push through plateaus and PR days.",
     "date": "June 5, 2026", "author": "Daniel Okafor", "read_time": "5 min read",
     "img": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=800&auto=format&fit=crop"},
    {"title": "Meal Prep Guide: One Sunday, One Week of Gains", "category": "nutrition",
     "excerpt": "A simple, repeatable system for prepping high-protein meals in under 90 minutes.",
     "date": "May 28, 2026", "author": "Elena Petrova", "read_time": "6 min read",
     "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format&fit=crop"},
]

FAQS = [
    {"q": "Do I need a long-term contract to join?", "a": "No. IRONCORE offers flexible month-to-month memberships alongside discounted annual plans — you're never locked in."},
    {"q": "Can I freeze or cancel my membership?", "a": "Yes, memberships can be paused for up to 60 days per year, and cancellation only requires 15 days' notice."},
    {"q": "Are personal trainers included in my plan?", "a": "Basic plans include full gym access; Pro and Elite plans include a set number of personal training sessions each month."},
    {"q": "What should I bring on my first visit?", "a": "Just comfortable workout clothes, athletic shoes, and a water bottle. We provide towels and sanitizing stations."},
    {"q": "Do you offer nutrition coaching?", "a": "Yes — our in-house dietitians build custom diet plans included with Pro and Elite memberships, or available a-la-carte."},
    {"q": "Is there an age requirement to join?", "a": "Members must be 16+ to train independently. Members aged 14-15 can train with a guardian's supervision."},
]

SERVICES = [
    {"icon": "fa-dumbbell", "title": "Strength Training", "desc": "Access to a full range of free weights, machines, and power racks."},
    {"icon": "fa-person-running", "title": "Cardio & HIIT", "desc": "Dedicated cardio zone plus scheduled high-intensity group classes."},
    {"icon": "fa-user-tie", "title": "Personal Training", "desc": "1-on-1 coaching tailored to your specific goals and experience level."},
    {"icon": "fa-bowl-food", "title": "Nutrition Coaching", "desc": "Custom diet plans built and adjusted by certified dietitians."},
    {"icon": "fa-people-group", "title": "Group Classes", "desc": "Spin, yoga, bootcamp and more — led by energetic certified instructors."},
    {"icon": "fa-spa", "title": "Recovery & Sauna", "desc": "Sauna, stretching zone, and massage therapy to speed up recovery."},
    {"icon": "fa-mobile-screen", "title": "Progress Tracking App", "desc": "Track workouts, nutrition, and body metrics from your phone."},
    {"icon": "fa-child-reaching", "title": "Youth Programs", "desc": "Safe, supervised strength & conditioning programs for teens."},
]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"


def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


CHEST_EXERCISES = [
    {
        "id": 1,
        "name": "Barbell Bench Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell + Bench",
        "image": img("Barbell_Bench_Press_-_Medium_Grip"),
        "description": "A compound pressing movement that develops the overall chest.",
        "steps": [
            "Lie flat on the bench.",
            "Grip the bar slightly wider than shoulder width.",
            "Lower the bar toward your mid chest.",
            "Press the bar upward while keeping your feet stable."
        ]
    },

    {
        "id": 2,
        "name": "Incline Barbell Bench Press",
        "type": "Gym",
        "muscle": "Upper Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell + Incline Bench",
        "image": img("Barbell_Incline_Bench_Press_-_Medium_Grip"),
        "description": "An incline pressing movement emphasizing the upper chest.",
        "steps": [
            "Set the bench to an incline.",
            "Grip the bar slightly wider than shoulder width.",
            "Lower the bar toward the upper chest.",
            "Press the bar upward under control."
        ]
    },

    {
        "id": 3,
        "name": "Decline Barbell Bench Press",
        "type": "Gym",
        "muscle": "Lower Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell + Decline Bench",
        "image": img("Decline_Barbell_Bench_Press"),
        "description": "A decline press that emphasizes the lower portion of the chest.",
        "steps": [
            "Secure yourself on a decline bench.",
            "Grip the bar evenly.",
            "Lower the bar toward the lower chest.",
            "Press it back to the starting position."
        ]
    },

    {
        "id": 4,
        "name": "Bench Press - Powerlifting",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–5",
        "reps": "5–8",
        "equipment": "Barbell + Bench",
        "image": img("Bench_Press_-_Powerlifting"),
        "description": "A heavy bench press variation for building pressing strength.",
        "steps": [
            "Position yourself securely on the bench.",
            "Retract your shoulder blades.",
            "Lower the bar under control.",
            "Drive the bar upward."
        ]
    },

    {
        "id": 5,
        "name": "Bench Press With Bands",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell + Resistance Bands",
        "image": img("Bench_Press_-_With_Bands"),
        "description": "Bench press performed with additional band resistance.",
        "steps": [
            "Secure the resistance bands.",
            "Lie on the bench and grip the bar.",
            "Lower the bar toward your chest.",
            "Press upward against the increasing resistance."
        ]
    },

    {
        "id": 6,
        "name": "Dumbbell Bench Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Dumbbells + Bench",
        "image": img("Dumbbell_Bench_Press"),
        "description": "Dumbbell pressing allows each side of the chest to work independently.",
        "steps": [
            "Lie flat on a bench with dumbbells.",
            "Start with the dumbbells above your chest.",
            "Lower them slowly.",
            "Press them back up."
        ]
    },

    {
        "id": 7,
        "name": "Incline Dumbbell Press",
        "type": "Gym",
        "muscle": "Upper Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Dumbbells + Incline Bench",
        "image": img("Incline_Dumbbell_Press"),
        "description": "A dumbbell pressing movement emphasizing the upper chest.",
        "steps": [
            "Set the bench to an incline.",
            "Hold dumbbells beside your chest.",
            "Press them upward.",
            "Lower them slowly."
        ]
    },

    {
        "id": 8,
        "name": "Dumbbell Flyes",
        "type": "Gym",
        "muscle": "Middle Chest",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Dumbbells + Bench",
        "image": img("Dumbbell_Flyes"),
        "description": "An isolation movement that stretches and contracts the chest.",
        "steps": [
            "Lie flat on a bench.",
            "Hold dumbbells above your chest.",
            "Open your arms with a slight bend in the elbows.",
            "Bring the dumbbells back together."
        ]
    },

    {
        "id": 9,
        "name": "Incline Dumbbell Flyes",
        "type": "Gym",
        "muscle": "Upper Chest",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Dumbbells + Incline Bench",
        "image": img("Incline_Dumbbell_Flyes"),
        "description": "Fly movement performed on an incline to emphasize the upper chest.",
        "steps": [
            "Set the bench to an incline.",
            "Hold dumbbells above your chest.",
            "Lower them outward slowly.",
            "Squeeze the upper chest as you bring them together."
        ]
    },

    {
        "id": 10,
        "name": "Cable Crossover",
        "type": "Gym",
        "muscle": "Middle Chest",
        "sets": "3–4",
        "reps": "10–15",
        "equipment": "Cable Machine",
        "image": img("Cable_Crossover"),
        "description": "Cable isolation exercise providing continuous chest tension.",
        "steps": [
            "Stand between the cable machines.",
            "Grab both handles.",
            "Bring your hands together in front of your chest.",
            "Slowly return to the starting position."
        ]
    },

   
    {
        "id": 11,
        "name": "Cable Chest Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Cable Machine",
        "image": img("Cable_Chest_Press"),
        "description": "A cable pressing movement that maintains resistance throughout the movement.",
        "steps": [
            "Position yourself between the cables.",
            "Hold the handles beside your chest.",
            "Press forward.",
            "Return slowly."
        ]
    },

    {
        "id": 12,
        "name": "Leverage Chest Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Chest Press Machine",
        "image": img("Leverage_Chest_Press"),
        "description": "Machine pressing exercise for controlled chest training.",
        "steps": [
            "Adjust the machine seat.",
            "Grip the handles.",
            "Press the handles forward.",
            "Return under control."
        ]
    },


    {
        "id": 13,
        "name": "Smith Machine Bench Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Smith Machine",
        "image": img("Smith_Machine_Bench_Press"),
        "description": "A guided barbell press using the Smith machine.",
        "steps": [
            "Set the bench under the Smith machine.",
            "Position the bar over your chest.",
            "Lower the bar.",
            "Press it upward."
        ]
    },

   
    {
        "id": 14,
        "name": "Smith Machine Incline Bench Press",
        "type": "Gym",
        "muscle": "Upper Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Smith Machine + Incline Bench",
        "image": img("Smith_Machine_Incline_Bench_Press"),
        "description": "Guided incline pressing for upper-chest development.",
        "steps": [
            "Set an incline bench inside the Smith machine.",
            "Grip the bar.",
            "Lower it toward your upper chest.",
            "Press upward."
        ]
    },

  
    {
        "id": 15,
        "name": "Chest Dips",
        "type": "Gym",
        "muscle": "Lower Chest",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Dip Station",
        "image": img("Dips_-_Chest_Version"),
        "description": "Bodyweight pressing exercise emphasizing the chest.",
        "steps": [
            "Grip the parallel bars.",
            "Lean your torso slightly forward.",
            "Lower your body.",
            "Push yourself back up."
        ]
    },

   
    {
        "id": 16,
        "name": "Bench Dips",
        "type": "Home",
        "muscle": "Lower Chest",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Bench or Chair",
        "image": img("Bench_Dips"),
        "description": "Bodyweight dip variation that can be performed at home.",
        "steps": [
            "Place your hands on a stable bench.",
            "Extend your legs forward.",
            "Lower your body.",
            "Push back upward."
        ]
    },

  
    {
        "id": 17,
        "name": "Push Ups",
        "type": "Home",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "10–20",
        "equipment": "Bodyweight",
        "image": img("Pushups"),
        "description": "Classic bodyweight chest exercise suitable for home training.",
        "steps": [
            "Start in a high plank position.",
            "Keep your body straight.",
            "Lower your chest toward the floor.",
            "Push back up."
        ]
    },

    {
        "id": 18,
        "name": "Incline Push Ups",
        "type": "Home",
        "muscle": "Upper Chest",
        "sets": "3",
        "reps": "12–20",
        "equipment": "Bench or Table",
        "image": img("Incline_Push-Up"),
        "description": "Beginner-friendly push-up variation using an elevated surface.",
        "steps": [
            "Place your hands on an elevated surface.",
            "Keep your body straight.",
            "Lower your chest toward the surface.",
            "Push back up."
        ]
    },

    {
        "id": 19,
        "name": "Decline Push Ups",
        "type": "Home",
        "muscle": "Upper Chest",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Bench or Chair",
        "image": img("Decline_Push-Up"),
        "description": "Push-up variation with elevated feet that increases upper-body demand.",
        "steps": [
            "Place your feet on a stable elevated surface.",
            "Put your hands on the floor.",
            "Lower your chest.",
            "Push back up."
        ]
    },


    {
        "id": 20,
        "name": "Dumbbell Floor Press",
        "type": "Home",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–15",
        "equipment": "Dumbbells",
        "image": img("Dumbbell_Floor_Press"),
        "description": "Chest press performed from the floor, useful for home workouts.",
        "steps": [
            "Lie on the floor with dumbbells.",
            "Start with the dumbbells above your chest.",
            "Lower until your upper arms touch the floor.",
            "Press upward."
        ]
    },


    {
        "id": 21,
        "name": "Floor Press",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell",
        "image": img("Floor_Press"),
        "description": "Pressing movement performed from the floor.",
        "steps": [
            "Lie on the floor beneath the bar.",
            "Grip the bar securely.",
            "Lower the bar until your upper arms touch the floor.",
            "Press the bar upward."
        ]
    },

    {
        "id": 22,
        "name": "Bent Arm Dumbbell Pullover",
        "type": "Gym",
        "muscle": "Chest",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Dumbbell + Bench",
        "image": img("Bent-Arm_Dumbbell_Pullover"),
        "description": "Pullover variation that involves the chest and upper-body muscles.",
        "steps": [
            "Lie on a bench holding a dumbbell.",
            "Position the dumbbell above your chest.",
            "Lower it behind your head with controlled movement.",
            "Bring it back above your chest."
        ]
    },

    
    {
        "id": 23,
        "name": "Bench Press With Chains",
        "type": "Gym",
        "muscle": "Overall Chest",
        "sets": "3–4",
        "reps": "6–10",
        "equipment": "Barbell + Chains",
        "image": img("Bench_Press_with_Chains"),
        "description": "Bench press variation using chains to increase resistance.",
        "steps": [
            "Set up the barbell and chains securely.",
            "Lie on the bench.",
            "Lower the bar toward your chest.",
            "Press the bar upward."
        ]
    },

 
    {
        "id": 24,
        "name": "Bodyweight Flyes",
        "type": "Home",
        "muscle": "Chest",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Bodyweight",
        "image": img("Bodyweight_Flyes"),
        "description": "Bodyweight chest fly variation for chest-focused training.",
        "steps": [
            "Set up in a stable bodyweight fly position.",
            "Keep your body controlled.",
            "Move your arms outward under control.",
            "Bring them back together while contracting the chest."
        ]
    }
]



IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"


def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


BACK_EXERCISES = [

    
    {
        "id": 1,
        "name": "Barbell Deadlift",
        "type": "Gym",
        "muscle": "Lower Back",
        "sets": "3–4",
        "reps": "6–10",
        "equipment": "Barbell",
        "image": img("Barbell_Deadlift"),
        "description": "A powerful compound exercise that develops the lower back, glutes and posterior chain.",
        "steps": [
            "Stand with your feet around hip width under the bar.",
            "Bend your hips and knees and grip the bar.",
            "Keep your back neutral and drive through your feet.",
            "Stand tall and lower the bar under control."
        ]
    },

  
    {
        "id": 2,
        "name": "Bent Over Barbell Row",
        "type": "Gym",
        "muscle": "Middle Back",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell",
        "image": img("Bent_Over_Barbell_Row"),
        "description": "A classic rowing movement for building the middle back and lats.",
        "steps": [
            "Hold the bar with an overhand grip.",
            "Bend forward while keeping your back straight.",
            "Pull the bar toward your stomach.",
            "Squeeze your back and slowly lower the bar."
        ]
    },


    {
        "id": 3,
        "name": "Bent-Arm Barbell Pullover",
        "type": "Gym",
        "muscle": "Lats",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Barbell + Bench",
        "image": img("Bent-Arm_Barbell_Pullover"),
        "description": "A pullover movement that emphasizes the lats while also involving the chest and shoulders.",
        "steps": [
            "Lie on a flat bench holding a barbell above your chest.",
            "Keep your elbows slightly bent.",
            "Lower the bar behind your head.",
            "Bring the bar back over your chest using your lats."
        ]
    },

    {
        "id": 4,
        "name": "Cable Deadlifts",
        "type": "Gym",
        "muscle": "Lower Back",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Cable Machine",
        "image": img("Cable_Deadlifts"),
        "description": "A cable-based hip-hinge exercise that trains the lower back and posterior chain.",
        "steps": [
            "Stand between the cable handles.",
            "Bend your hips and knees to grab the handles.",
            "Drive through your heels and extend your hips.",
            "Return the handles under control."
        ]
    },


    {
        "id": 5,
        "name": "Cable Incline Pushdown",
        "type": "Gym",
        "muscle": "Lats",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable Machine",
        "image": img("Cable_Incline_Pushdown"),
        "description": "An isolation-style movement designed to keep tension on the lat muscles.",
        "steps": [
            "Lie on an incline bench facing away from the cable.",
            "Grip the cable attachment.",
            "Move the bar in an arc toward your thighs.",
            "Return slowly while maintaining lat tension."
        ]
    },


    {
        "id": 6,
        "name": "Inverted Row with Straps",
        "type": "Home",
        "muscle": "Upper Back",
        "sets": "3–4",
        "reps": "8–15",
        "equipment": "Suspension Straps",
        "image": img("Inverted_Row_with_Straps"),
        "description": "A bodyweight pulling exercise that trains the upper back and lats.",
        "steps": [
            "Hold the straps and lean back with your body straight.",
            "Keep your core tight.",
            "Pull your chest toward your hands.",
            "Lower yourself slowly."
        ]
    },


    {
        "id": 7,
        "name": "Kipping Muscle Up",
        "type": "Gym",
        "muscle": "Lats",
        "sets": "3",
        "reps": "5–10",
        "equipment": "Pull-Up Bar",
        "image": img("Kipping_Muscle_Up"),
        "description": "An advanced bodyweight movement requiring strong lats, shoulders and upper body control.",
        "steps": [
            "Hang from the bar with a secure grip.",
            "Use a controlled kip to generate movement.",
            "Pull your chest toward the bar.",
            "Transition your body above the bar."
        ]
    },

    {
        "id": 8,
        "name": "Kneeling High Pulley Row",
        "type": "Gym",
        "muscle": "Upper Back",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Cable Machine",
        "image": img("Kneeling_High_Pulley_Row"),
        "description": "A cable rowing movement that emphasizes the upper and middle back.",
        "steps": [
            "Kneel several feet from the high pulley.",
            "Hold the rope with both hands.",
            "Pull the rope toward your upper chest.",
            "Slowly extend your arms again."
        ]
    },


    {
        "id": 9,
        "name": "Pullups",
        "type": "Home",
        "muscle": "Lats",
        "sets": "3–4",
        "reps": "6–12",
        "equipment": "Pull-Up Bar",
        "image": img("Pullups"),
        "description": "One of the best bodyweight exercises for developing the lats and upper back.",
        "steps": [
            "Grip the pull-up bar with your palms facing forward.",
            "Start from a controlled hanging position.",
            "Pull your chest toward the bar.",
            "Lower yourself slowly until your arms are extended."
        ]
    },

  
    {
        "id": 10,
        "name": "Scapular Pull-Up",
        "type": "Home",
        "muscle": "Upper Back",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Pull-Up Bar",
        "image": img("Scapular_Pull-Up"),
        "description": "A controlled pulling exercise that strengthens the scapular muscles and supports pull-up performance.",
        "steps": [
            "Hang from the pull-up bar.",
            "Keep your arms straight.",
            "Pull your shoulder blades down and back.",
            "Return to the relaxed hanging position."
        ]
    },

    {
        "id": 11,
        "name": "Seated Cable Rows",
        "type": "Gym",
        "muscle": "Middle Back",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Cable Machine",
        "image": img("Seated_Cable_Rows"),
        "description": "A popular horizontal pulling exercise for building thickness in the middle back.",
        "steps": [
            "Sit upright with your feet against the platform.",
            "Hold the cable handle with both hands.",
            "Pull the handle toward your abdomen.",
            "Squeeze your shoulder blades and slowly release."
        ]
    },

 
    {
        "id": 12,
        "name": "Alternating Kettlebell Row",
        "type": "Home",
        "muscle": "Middle Back",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Kettlebells",
        "image": img("Alternating_Kettlebell_Row"),
        "description": "A unilateral rowing exercise that develops the middle back and lats.",
        "steps": [
            "Place two kettlebells in front of you.",
            "Hinge forward while keeping your back straight.",
            "Row one kettlebell toward your body.",
            "Lower it and repeat with the opposite arm."
        ]
    },

    {
        "id": 13,
        "name": "Alternating Renegade Row",
        "type": "Home",
        "muscle": "Upper Back",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Kettlebells",
        "image": img("Alternating_Renegade_Row"),
        "description": "A challenging rowing movement combining back training with core stability.",
        "steps": [
            "Start in a strong plank position holding the kettlebells.",
            "Keep your hips stable.",
            "Row one kettlebell toward your ribs.",
            "Lower it and alternate sides."
        ]
    },

    {
        "id": 14,
        "name": "One-Arm Kettlebell Row",
        "type": "Home",
        "muscle": "Middle Back",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Kettlebell",
        "image": img("One-Arm_Kettlebell_Row"),
        "description": "A single-arm row that targets the middle back and lats.",
        "steps": [
            "Place the kettlebell in front of your feet.",
            "Hinge forward while keeping your back straight.",
            "Pull the kettlebell toward your stomach.",
            "Lower it slowly and repeat."
        ]
    },

    {
        "id": 15,
        "name": "Middle Back Shrug",
        "type": "Gym",
        "muscle": "Middle Back",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Dumbbells + Bench",
        "image": img("Middle_Back_Shrug"),
        "description": "A controlled upper-back movement focusing on squeezing the shoulder blades together.",
        "steps": [
            "Lie face down on an incline bench.",
            "Hold a dumbbell in each hand.",
            "Pull your shoulder blades together.",
            "Return your arms to the starting position."
        ]
    },

    {
        "id": 16,
        "name": "Mixed Grip Chin",
        "type": "Home",
        "muscle": "Middle Back",
        "sets": "3",
        "reps": "6–10",
        "equipment": "Pull-Up Bar",
        "image": img("Mixed_Grip_Chin"),
        "description": "An advanced chin-up variation that works the middle back and lats.",
        "steps": [
            "Grip the bar with one palm facing you and one facing away.",
            "Hang with your arms extended.",
            "Pull your chest toward the bar.",
            "Lower yourself under control."
        ]
    },

    {
        "id": 17,
        "name": "Shotgun Row",
        "type": "Gym",
        "muscle": "Lats",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Cable Machine",
        "image": img("Shotgun_Row"),
        "description": "A single-arm cable rowing movement that emphasizes the lats and middle back.",
        "steps": [
            "Attach a single handle to a low cable.",
            "Stand back in a split stance.",
            "Pull the handle toward your side.",
            "Return slowly to the starting position."
        ]
    },


    {
        "id": 18,
        "name": "Sled Row",
        "type": "Gym",
        "muscle": "Upper Back",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Sled",
        "image": img("Sled_Row"),
        "description": "A resistance-based rowing movement that trains the upper back and pulling muscles.",
        "steps": [
            "Attach the handles to the sled.",
            "Take a stable stance.",
            "Pull the sled toward you using your back.",
            "Control the sled throughout the movement."
        ]
    },

    {
        "id": 19,
        "name": "Band Good Morning Pull Through",
        "type": "Home",
        "muscle": "Lower Back",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Resistance Band",
        "image": img("Band_Good_Morning_Pull_Through"),
        "description": "A resistance-band hip hinge that trains the lower back and posterior chain.",
        "steps": [
            "Secure the band behind you.",
            "Place the band around your neck or upper back safely.",
            "Hinge forward while keeping your back neutral.",
            "Drive your hips forward to stand."
        ]
    },

   
    {
        "id": 20,
        "name": "Band Pull Apart",
        "type": "Home",
        "muscle": "Upper Back",
        "sets": "3",
        "reps": "12–20",
        "equipment": "Resistance Band",
        "image": img("Band_Pull_Apart"),
        "description": "A simple resistance-band exercise for the upper back and rear shoulder area.",
        "steps": [
            "Hold the band in front of your chest.",
            "Keep your arms mostly straight.",
            "Pull the band apart by moving your hands outward.",
            "Slowly return to the starting position."
        ]
    },
]


IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


LEGS_EXERCISES = [

    {
        "id": 1,
        "name": "Barbell Squat",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell",
        "image": img("Barbell_Squat"),
        "description": "A compound leg exercise that develops the quadriceps, glutes and hamstrings.",
        "steps": [
            "Stand with your feet around shoulder-width apart.",
            "Place the barbell securely across your upper back.",
            "Brace your core and keep your chest up.",
            "Bend your knees and hips to lower into a squat.",
            "Drive through your feet to return to standing."
        ]
    },

    {
        "id": 2,
        "name": "Barbell Full Squat",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell + Rack",
        "image": img("Barbell_Full_Squat"),
        "description": "A deep barbell squat variation that strongly trains the quads and glutes.",
        "steps": [
            "Set the bar at an appropriate height in a squat rack.",
            "Place the bar across your upper back.",
            "Stand with your feet at a comfortable width.",
            "Lower your hips under control.",
            "Drive through your heels to stand."
        ]
    },

    {
        "id": 3,
        "name": "Barbell Lunge",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "8–12 each leg",
        "equipment": "Barbell",
        "image": img("Barbell_Lunge"),
        "description": "A unilateral exercise that develops leg strength, balance and glute activation.",
        "steps": [
            "Place the barbell across your upper back.",
            "Stand upright with your feet together.",
            "Step forward with one leg.",
            "Lower your body until both knees are comfortably bent.",
            "Push through your front foot and return."
        ]
    },

    {
        "id": 4,
        "name": "Barbell Walking Lunge",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "10–15 each leg",
        "equipment": "Barbell",
        "image": img("Barbell_Walking_Lunge"),
        "description": "A walking lunge variation that builds strength and coordination throughout the legs.",
        "steps": [
            "Place the barbell securely across your upper back.",
            "Stand tall with your core braced.",
            "Step forward into a lunge.",
            "Push through the front foot.",
            "Continue walking and alternate legs."
        ]
    },

    {
        "id": 5,
        "name": "Barbell Step Ups",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "8–12 each leg",
        "equipment": "Barbell + Step",
        "image": img("Barbell_Step_Ups"),
        "description": "A unilateral movement that targets the quads and glutes while improving balance.",
        "steps": [
            "Place the barbell across your upper back.",
            "Stand behind a stable elevated platform.",
            "Place one foot on the platform.",
            "Push through that foot to step up.",
            "Step down under control and switch legs."
        ]
    },

    {
        "id": 6,
        "name": "Barbell Glute Bridge",
        "type": "Gym",
        "muscle": "Glutes + Hamstrings",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Barbell",
        "image": img("Barbell_Glute_Bridge"),
        "description": "A loaded hip-extension exercise that emphasizes the glutes and hamstrings.",
        "steps": [
            "Lie on your back with the barbell positioned over your hips.",
            "Keep your knees bent and feet flat.",
            "Brace your core.",
            "Drive through your heels and raise your hips.",
            "Squeeze your glutes at the top and lower slowly."
        ]
    },

    {
        "id": 7,
        "name": "Leg Press",
        "type": "Gym",
        "muscle": "Quadriceps",
        "sets": "3–4",
        "reps": "10–15",
        "equipment": "Leg Press Machine",
        "image": img("Leg_Press"),
        "description": "A machine-based compound exercise primarily targeting the quadriceps.",
        "steps": [
            "Sit securely on the leg press machine.",
            "Place your feet firmly on the platform.",
            "Lower the platform under control.",
            "Push through your feet to extend your legs.",
            "Avoid aggressively locking your knees."
        ]
    },

    {
        "id": 8,
        "name": "Leg Extension",
        "type": "Gym",
        "muscle": "Quadriceps",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Leg Extension Machine",
        "image": img("Leg_Extensions"),
        "description": "An isolation exercise designed to focus directly on the quadriceps.",
        "steps": [
            "Sit comfortably on the leg extension machine.",
            "Place your ankles behind the pads.",
            "Extend your knees under control.",
            "Squeeze your quadriceps at the top.",
            "Lower the weight slowly."
        ]
    },

    {
        "id": 9,
        "name": "Lying Leg Curl",
        "type": "Gym",
        "muscle": "Hamstrings",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Leg Curl Machine",
        "image": img("Lying_Leg_Curls"),
        "description": "An isolation exercise that targets the hamstrings.",
        "steps": [
            "Lie face down on the machine.",
            "Position your ankles beneath the pads.",
            "Curl your heels toward your glutes.",
            "Squeeze your hamstrings.",
            "Lower the weight slowly."
        ]
    },

    {
        "id": 10,
        "name": "Dumbbell Step Ups",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "10–12 each leg",
        "equipment": "Dumbbells + Bench",
        "image": img("Dumbbell_Step_Ups"),
        "description": "A unilateral dumbbell exercise that develops the quads and glutes.",
        "steps": [
            "Hold a dumbbell in each hand.",
            "Stand in front of a stable bench or step.",
            "Place one foot on the platform.",
            "Push through that foot to step up.",
            "Step down and alternate legs."
        ]
    },



    {
        "id": 11,
        "name": "Bodyweight Squat",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "15–20",
        "equipment": "Bodyweight",
        "image": img("Bodyweight_Squat"),
        "description": "A simple bodyweight exercise for developing basic lower-body strength.",
        "steps": [
            "Stand with your feet around shoulder-width apart.",
            "Keep your chest up and core tight.",
            "Push your hips backward.",
            "Bend your knees and lower your body.",
            "Push through your feet to stand."
        ]
    },

    {
        "id": 12,
        "name": "Bodyweight Walking Lunge",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "10–15 each leg",
        "equipment": "Bodyweight",
        "image": img("Bodyweight_Walking_Lunge"),
        "description": "A bodyweight walking movement that develops the quads, glutes and balance.",
        "steps": [
            "Stand upright with your feet together.",
            "Step forward with one leg.",
            "Lower your hips into a lunge.",
            "Push through the front foot.",
            "Continue forward while alternating legs."
        ]
    },

    {
        "id": 13,
        "name": "Butt Lift Bridge",
        "type": "Home",
        "muscle": "Glutes + Hamstrings",
        "sets": "3",
        "reps": "15–20",
        "equipment": "Bodyweight",
        "image": img("Butt_Lift_Bridge"),
        "description": "A bodyweight bridge movement that strengthens the glutes and hamstrings.",
        "steps": [
            "Lie on your back with your knees bent.",
            "Keep your feet flat on the floor.",
            "Drive through your heels.",
            "Raise your hips toward the ceiling.",
            "Squeeze your glutes and lower slowly."
        ]
    },

    {
        "id": 14,
        "name": "Freehand Jump Squat",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Bodyweight",
        "image": img("Freehand_Jump_Squat"),
        "description": "An explosive bodyweight exercise for developing lower-body power.",
        "steps": [
            "Stand with your feet shoulder-width apart.",
            "Lower into a comfortable squat.",
            "Drive through your feet and jump upward.",
            "Land softly with bent knees.",
            "Immediately prepare for the next repetition."
        ]
    },

    {
        "id": 15,
        "name": "Bench Jump",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Stable Bench",
        "image": img("Bench_Jump"),
        "description": "An explosive jumping exercise that trains the legs and lower-body power.",
        "steps": [
            "Stand facing a stable bench.",
            "Bend your knees slightly.",
            "Swing your arms and jump onto the bench.",
            "Land with both feet securely.",
            "Step down carefully and repeat."
        ]
    },

    {
        "id": 16,
        "name": "Box Jump",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Stable Box",
        "image": img("Box_Jump_Multiple_Response"),
        "description": "A plyometric exercise that develops explosive leg power.",
        "steps": [
            "Stand facing a stable box.",
            "Bend your knees and hips.",
            "Jump explosively onto the box.",
            "Land softly with both feet.",
            "Step down carefully."
        ]
    },

    {
        "id": 17,
        "name": "Front Leg Raises",
        "type": "Home",
        "muscle": "Quadriceps + Hip Flexors",
        "sets": "3",
        "reps": "12–15 each leg",
        "equipment": "Bodyweight",
        "image": img("Front_Leg_Raises"),
        "description": "A simple leg-raising movement that trains the front of the legs and hip flexors.",
        "steps": [
            "Stand upright with good posture.",
            "Hold a stable surface if needed.",
            "Raise one leg straight in front of you.",
            "Pause briefly at the top.",
            "Lower the leg slowly and switch sides."
        ]
    },

    {
        "id": 18,
        "name": "Single Leg Glute Bridge",
        "type": "Home",
        "muscle": "Glutes + Hamstrings",
        "sets": "3",
        "reps": "10–15 each leg",
        "equipment": "Bodyweight",
        "image": img("Single_Leg_Glute_Bridge"),
        "description": "A unilateral bridge variation that strengthens the glutes and hamstrings.",
        "steps": [
            "Lie on your back with one knee bent.",
            "Extend the opposite leg upward.",
            "Drive through the foot on the floor.",
            "Raise your hips while keeping your core tight.",
            "Lower slowly and repeat on the other side."
        ]
    },

    {
        "id": 19,
        "name": "Split Squats",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "10–15 each leg",
        "equipment": "Bodyweight",
        "image": img("Split_Squats"),
        "description": "A unilateral squat variation that develops the quads, glutes and balance.",
        "steps": [
            "Take a staggered stance with one foot forward.",
            "Keep your torso upright.",
            "Lower your rear knee toward the floor.",
            "Push through your front foot.",
            "Complete your repetitions and switch legs."
        ]
    },

    {
        "id": 20,
        "name": "Standing Long Jump",
        "type": "Home",
        "muscle": "Quadriceps + Glutes + Calves",
        "sets": "3",
        "reps": "6–10",
        "equipment": "Bodyweight",
        "image": img("Standing_Long_Jump"),
        "description": "An explosive bodyweight exercise that develops lower-body power and coordination.",
        "steps": [
            "Stand with your feet around shoulder-width apart.",
            "Bend your knees and swing your arms backward.",
            "Explosively extend your hips, knees and ankles.",
            "Jump forward as far as comfortably possible.",
            "Land softly and regain your balance."
        ]
    }

]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


SHOULDERS_EXERCISES = [

    {
        "id": 1,
        "name": "Dumbbell Shoulder Press",
        "type": "Gym",
        "muscle": "Overall Shoulders",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Dumbbells + Bench",
        "image": img("Dumbbell_Shoulder_Press"),
        "description": "A fundamental pressing exercise that develops the front and side deltoids.",
        "steps": [
            "Sit on a bench with back support.",
            "Hold the dumbbells at shoulder height.",
            "Keep your palms facing forward.",
            "Press the dumbbells overhead.",
            "Lower them slowly back to shoulder level."
        ]
    },

    {
        "id": 2,
        "name": "One-Arm Dumbbell Shoulder Press",
        "type": "Gym",
        "muscle": "Deltoids",
        "sets": "3",
        "reps": "8–12 each arm",
        "equipment": "Dumbbell",
        "image": img("Dumbbell_One-Arm_Shoulder_Press"),
        "description": "A unilateral shoulder press that develops the deltoids and improves stability.",
        "steps": [
            "Hold one dumbbell at shoulder height.",
            "Keep your torso upright.",
            "Press the dumbbell overhead.",
            "Pause briefly at the top.",
            "Lower it under control and switch arms."
        ]
    },

    {
        "id": 3,
        "name": "One-Arm Dumbbell Upright Row",
        "type": "Gym",
        "muscle": "Side Delts + Traps",
        "sets": "3",
        "reps": "10–12 each arm",
        "equipment": "Dumbbell",
        "image": img("Dumbbell_One-Arm_Upright_Row"),
        "description": "A unilateral pulling movement that targets the side shoulders and traps.",
        "steps": [
            "Stand upright holding a dumbbell.",
            "Keep the dumbbell close to your body.",
            "Drive your elbow upward.",
            "Raise the dumbbell toward chin level.",
            "Lower it slowly."
        ]
    },

    {
        "id": 4,
        "name": "Dumbbell Raise",
        "type": "Gym",
        "muscle": "Side Delts",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Dumbbells",
        "image": img("Dumbbell_Raise"),
        "description": "A shoulder isolation movement that emphasizes the lateral deltoids.",
        "steps": [
            "Stand upright holding dumbbells.",
            "Keep a slight bend in your elbows.",
            "Raise the dumbbells upward.",
            "Drive the movement with your elbows.",
            "Lower the weights slowly."
        ]
    },

    {
        "id": 5,
        "name": "Dumbbell Scaption",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Light Dumbbells",
        "image": img("Dumbbell_Scaption"),
        "description": "A controlled shoulder exercise that strengthens the deltoids and shoulder stabilizers.",
        "steps": [
            "Hold light dumbbells beside your body.",
            "Keep your thumbs pointing upward.",
            "Raise your arms slightly forward and outward.",
            "Continue until your arms are approximately parallel to the floor.",
            "Lower them slowly."
        ]
    },

    {
        "id": 6,
        "name": "Double Kettlebell Jerk",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "6–10",
        "equipment": "Kettlebells",
        "image": img("Double_Kettlebell_Jerk"),
        "description": "An explosive overhead movement that develops shoulder power and strength.",
        "steps": [
            "Hold a kettlebell in each hand.",
            "Clean the kettlebells to shoulder height.",
            "Bend your knees slightly.",
            "Drive through your legs and press overhead.",
            "Lower the kettlebells carefully."
        ]
    },

    {
        "id": 7,
        "name": "Double Kettlebell Push Press",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Kettlebells",
        "image": img("Double_Kettlebell_Push_Press"),
        "description": "A powerful pressing exercise that uses the legs to assist the shoulders.",
        "steps": [
            "Hold both kettlebells at shoulder height.",
            "Bend your knees slightly.",
            "Drive upward through your legs.",
            "Press both kettlebells overhead.",
            "Return them to shoulder height."
        ]
    },

    {
        "id": 8,
        "name": "Double Kettlebell Snatch",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "6–10",
        "equipment": "Kettlebells",
        "image": img("Double_Kettlebell_Snatch"),
        "description": "An explosive full-body movement with strong overhead shoulder involvement.",
        "steps": [
            "Place the kettlebells behind your feet.",
            "Bend your knees and grip them.",
            "Swing the kettlebells between your legs.",
            "Drive your hips forward.",
            "Lock the kettlebells overhead."
        ]
    },

    {
        "id": 9,
        "name": "Alternating Cable Shoulder Press",
        "type": "Gym",
        "muscle": "Deltoids",
        "sets": "3",
        "reps": "10–12 each arm",
        "equipment": "Cable Machine",
        "image": img("Alternating_Cable_Shoulder_Press"),
        "description": "An alternating cable pressing movement for developing shoulder strength.",
        "steps": [
            "Set the cable handles at a suitable height.",
            "Hold the handles at shoulder level.",
            "Keep your chest upright.",
            "Press one handle overhead.",
            "Return and alternate arms."
        ]
    },

    {
        "id": 10,
        "name": "Seated Barbell Military Press",
        "type": "Gym",
        "muscle": "Overall Shoulders",
        "sets": "3–4",
        "reps": "6–10",
        "equipment": "Barbell + Bench",
        "image": img("Seated_Barbell_Military_Press"),
        "description": "A classic barbell pressing movement for building overall shoulder strength.",
        "steps": [
            "Sit on a military press bench.",
            "Grip the bar slightly wider than shoulder width.",
            "Start with the bar around shoulder level.",
            "Press it overhead.",
            "Lower it slowly to the starting position."
        ]
    },

    {
        "id": 11,
        "name": "Seated Cable Shoulder Press",
        "type": "Gym",
        "muscle": "Deltoids",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Cable Machine",
        "image": img("Seated_Cable_Shoulder_Press"),
        "description": "A cable pressing exercise that maintains constant tension on the shoulders.",
        "steps": [
            "Sit securely at the cable station.",
            "Hold the handles at shoulder height.",
            "Keep your chest up.",
            "Press the handles overhead.",
            "Return slowly to the starting position."
        ]
    },

    {
        "id": 12,
        "name": "Seated Bent-Over Rear Delt Raise",
        "type": "Gym",
        "muscle": "Rear Delts",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Dumbbells + Bench",
        "image": img("Seated_Bent-Over_Rear_Delt_Raise"),
        "description": "An isolation exercise focused on the rear deltoids.",
        "steps": [
            "Sit at the end of a bench.",
            "Hold a dumbbell in each hand.",
            "Lean your torso forward.",
            "Raise the dumbbells out to your sides.",
            "Lower them slowly."
        ]
    },

    {
        "id": 13,
        "name": "Side Lateral Raise",
        "type": "Gym",
        "muscle": "Side Delts",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Dumbbells",
        "image": img("Side_Lateral_Raise"),
        "description": "One of the most popular isolation exercises for developing wider-looking shoulders.",
        "steps": [
            "Stand upright with dumbbells at your sides.",
            "Keep your elbows slightly bent.",
            "Raise the dumbbells outward.",
            "Stop around shoulder height.",
            "Lower them slowly."
        ]
    },

    {
        "id": 14,
        "name": "Side Laterals to Front Raise",
        "type": "Gym",
        "muscle": "Side + Front Delts",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Dumbbells",
        "image": img("Side_Laterals_to_Front_Raise"),
        "description": "A combined raise movement that trains different portions of the deltoids.",
        "steps": [
            "Hold dumbbells at your sides.",
            "Raise the weights toward the front.",
            "Move them through the lateral position.",
            "Keep your torso stable.",
            "Lower the dumbbells under control."
        ]
    },

    {
        "id": 15,
        "name": "Alternating Deltoid Raise",
        "type": "Gym",
        "muscle": "Front + Side Delts",
        "sets": "3",
        "reps": "10–12 each side",
        "equipment": "Dumbbells",
        "image": img("Alternating_Deltoid_Raise"),
        "description": "An alternating raise that works the front and lateral portions of the shoulders.",
        "steps": [
            "Stand holding dumbbells at your sides.",
            "Raise one dumbbell in front of you.",
            "Lower it back down.",
            "Raise the other dumbbell laterally.",
            "Continue alternating."
        ]
    },

    {
        "id": 16,
        "name": "Alternating Kettlebell Press",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "8–12 each arm",
        "equipment": "Kettlebells",
        "image": img("Alternating_Kettlebell_Press"),
        "description": "An alternating overhead kettlebell press for shoulder strength and stability.",
        "steps": [
            "Clean both kettlebells to shoulder level.",
            "Press one kettlebell overhead.",
            "Keep the opposite kettlebell stable.",
            "Lower the first kettlebell.",
            "Press with the opposite arm."
        ]
    },

    {
        "id": 17,
        "name": "Anti-Gravity Press",
        "type": "Gym",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Barbell + Bench",
        "image": img("Anti-Gravity_Press"),
        "description": "A pressing movement that challenges the shoulders and upper-body stability.",
        "steps": [
            "Position yourself on an incline bench.",
            "Grip the bar securely.",
            "Start with the bar near your upper body.",
            "Press the bar forward.",
            "Return it under control."
        ]
    },


    # =========================================================
    # HOME / NO-MACHINE EXERCISES
    # =========================================================

    {
        "id": 18,
        "name": "Shoulder Press With Bands",
        "type": "Home",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Resistance Band",
        "image": img("Shoulder_Press_-_With_Bands"),
        "description": "A resistance-band shoulder press that can be performed at home.",
        "steps": [
            "Stand on the resistance band.",
            "Hold the handles at shoulder height.",
            "Keep your palms facing forward.",
            "Press the handles overhead.",
            "Lower them slowly."
        ]
    },

    {
        "id": 19,
        "name": "Shoulder Circles",
        "type": "Home",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Bodyweight",
        "image": img("Shoulder_Circles"),
        "description": "A simple shoulder mobility exercise that can be performed without equipment.",
        "steps": [
            "Stand or sit comfortably.",
            "Relax your shoulders.",
            "Roll your shoulders forward and upward.",
            "Continue the circle backward and downward.",
            "Reverse the direction."
        ]
    },

    {
        "id": 20,
        "name": "Arm Circles",
        "type": "Home",
        "muscle": "Shoulders",
        "sets": "3",
        "reps": "15–20",
        "equipment": "Bodyweight",
        "image": img("Arm_Circles"),
        "description": "A simple bodyweight movement for shoulder mobility and warm-up.",
        "steps": [
            "Stand upright.",
            "Extend your arms out to your sides.",
            "Make small circular movements.",
            "Gradually increase the circle size.",
            "Reverse the direction."
        ]
    }

]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


ARMS_EXERCISES = [

    {
        "id": 1,
        "name": "Alternate Hammer Curl",
        "type": "Gym",
        "muscle": "Biceps + Forearms",
        "sets": "3",
        "reps": "10–12 each arm",
        "equipment": "Dumbbells",
        "image": img("Alternate_Hammer_Curl"),
        "description": "A neutral-grip curl that develops the biceps and forearms.",
        "steps": [
            "Stand upright holding a dumbbell in each hand.",
            "Keep your palms facing your torso.",
            "Curl one dumbbell toward your shoulder.",
            "Keep your upper arm stationary.",
            "Lower it slowly and alternate arms."
        ]
    },

    {
        "id": 2,
        "name": "Alternate Incline Dumbbell Curl",
        "type": "Gym",
        "muscle": "Biceps",
        "sets": "3",
        "reps": "8–12 each arm",
        "equipment": "Dumbbells + Incline Bench",
        "image": img("Alternate_Incline_Dumbbell_Curl"),
        "description": "An incline curl variation that places the biceps under a greater stretch.",
        "steps": [
            "Sit on an incline bench.",
            "Hold a dumbbell in each hand.",
            "Let your arms hang naturally.",
            "Curl one dumbbell toward your shoulder.",
            "Lower it slowly and alternate arms."
        ]
    },

    {
        "id": 3,
        "name": "Barbell Curl",
        "type": "Gym",
        "muscle": "Biceps",
        "sets": "3–4",
        "reps": "8–12",
        "equipment": "Barbell",
        "image": img("Barbell_Curl"),
        "description": "A classic barbell exercise for building overall biceps strength and size.",
        "steps": [
            "Stand upright holding the barbell.",
            "Use an underhand grip.",
            "Keep your elbows close to your body.",
            "Curl the bar toward your shoulders.",
            "Lower the bar under control."
        ]
    },

    {
        "id": 4,
        "name": "Barbell Curls Lying Against An Incline",
        "type": "Gym",
        "muscle": "Biceps",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Barbell + Incline Bench",
        "image": img("Barbell_Curls_Lying_Against_An_Incline"),
        "description": "An incline-supported barbell curl that trains the biceps while limiting body movement.",
        "steps": [
            "Lie against an incline bench.",
            "Hold the barbell with an underhand grip.",
            "Let your arms hang downward.",
            "Curl the bar while keeping your upper arms still.",
            "Lower the bar under control."
        ]
    },

    {
        "id": 5,
        "name": "Preacher Curl",
        "type": "Gym",
        "muscle": "Biceps",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Preacher Bench",
        "image": img("Preacher_Curl"),
        "description": "An isolation exercise that supports the upper arms while training the biceps.",
        "steps": [
            "Sit at the preacher bench.",
            "Place your upper arms on the pad.",
            "Grip the bar.",
            "Curl the weight upward.",
            "Lower it slowly."
        ]
    },

    {
        "id": 6,
        "name": "Cable Hammer Curl",
        "type": "Gym",
        "muscle": "Biceps + Forearms",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable + Rope",
        "image": img("Cable_Hammer_Curls_-_Rope_Attachment"),
        "description": "A cable hammer curl using a rope attachment to train the biceps and forearms.",
        "steps": [
            "Attach a rope to a low cable pulley.",
            "Stand upright and hold the rope with a neutral grip.",
            "Keep your elbows close to your body.",
            "Curl the rope toward your shoulders.",
            "Lower the rope slowly."
        ]
    },

    {
        "id": 7,
        "name": "Cable Preacher Curl",
        "type": "Gym",
        "muscle": "Biceps + Forearms",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Cable + Preacher Bench",
        "image": img("Cable_Preacher_Curl"),
        "description": "A cable preacher curl that maintains resistance throughout the biceps movement.",
        "steps": [
            "Place a preacher bench in front of a low cable.",
            "Attach a straight bar.",
            "Place your upper arms on the preacher pad.",
            "Curl the bar toward your shoulders.",
            "Lower the bar slowly."
        ]
    },

    {
        "id": 8,
        "name": "Lying Dumbbell Triceps Extension",
        "type": "Gym",
        "muscle": "Triceps",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Dumbbells + Bench",
        "image": img("Lying_Dumbbell_Tricep_Extension"),
        "description": "A lying dumbbell extension that directly trains the triceps.",
        "steps": [
            "Lie flat on a bench.",
            "Hold the dumbbells above your chest.",
            "Keep your upper arms relatively still.",
            "Bend your elbows and lower the dumbbells.",
            "Extend your elbows to return."
        ]
    },

    {
        "id": 9,
        "name": "Cable Rope Overhead Triceps Extension",
        "type": "Gym",
        "muscle": "Triceps",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable + Rope",
        "image": img("Cable_Rope_Overhead_Triceps_Extension"),
        "description": "An overhead cable movement that emphasizes the triceps.",
        "steps": [
            "Attach a rope to a low cable.",
            "Face away from the machine.",
            "Hold the rope behind your head.",
            "Extend your elbows upward.",
            "Return slowly."
        ]
    },

    {
        "id": 10,
        "name": "Triceps Pushdown - V-Bar",
        "type": "Gym",
        "muscle": "Triceps",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable + V-Bar",
        "image": img("Triceps_Pushdown_-_V-Bar_Attachment"),
        "description": "A cable pushdown using a V-bar to develop the triceps.",
        "steps": [
            "Stand facing the cable machine.",
            "Grip the V-bar.",
            "Keep your elbows close to your body.",
            "Push the bar downward.",
            "Return slowly to the starting position."
        ]
    },

    {
        "id": 11,
        "name": "Reverse Barbell Curl",
        "type": "Gym",
        "muscle": "Forearms + Biceps",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Barbell",
        "image": img("Reverse_Barbell_Curl"),
        "description": "A reverse-grip barbell curl that emphasizes the forearms and brachialis.",
        "steps": [
            "Hold the barbell with an overhand grip.",
            "Keep your elbows close to your sides.",
            "Curl the bar upward.",
            "Squeeze the biceps and forearms.",
            "Lower the bar slowly."
        ]
    },

    {
        "id": 12,
        "name": "Reverse Cable Curl",
        "type": "Gym",
        "muscle": "Forearms + Biceps",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable",
        "image": img("Reverse_Cable_Curl"),
        "description": "A reverse-grip cable curl that keeps continuous tension on the arms.",
        "steps": [
            "Attach a straight bar to a low cable.",
            "Use an overhand grip.",
            "Keep your elbows close to your body.",
            "Curl the bar upward.",
            "Lower it under control."
        ]
    },

    {
        "id": 13,
        "name": "Cable Wrist Curl",
        "type": "Gym",
        "muscle": "Forearms",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Cable",
        "image": img("Cable_Wrist_Curl"),
        "description": "A cable isolation exercise for strengthening the forearm muscles.",
        "steps": [
            "Place a bench in front of a low cable.",
            "Hold the cable bar with your palms facing upward.",
            "Rest your forearms on your thighs.",
            "Curl your wrists upward.",
            "Lower the weight slowly."
        ]
    },

    {
        "id": 14,
        "name": "Seated Dumbbell Curl",
        "type": "Gym",
        "muscle": "Biceps",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Dumbbells + Bench",
        "image": img("Seated_Dumbbell_Curl"),
        "description": "A seated dumbbell curl that trains the biceps while reducing body swing.",
        "steps": [
            "Sit upright on a bench.",
            "Hold a dumbbell in each hand.",
            "Keep your elbows close to your sides.",
            "Curl the dumbbells toward your shoulders.",
            "Lower them slowly."
        ]
    },

    {
        "id": 15,
        "name": "Hammer Curls",
        "type": "Gym",
        "muscle": "Biceps + Forearms",
        "sets": "3",
        "reps": "10–12",
        "equipment": "Dumbbells",
        "image": img("Hammer_Curls"),
        "description": "A neutral-grip dumbbell curl that targets the biceps and forearms.",
        "steps": [
            "Stand upright with a dumbbell in each hand.",
            "Keep your palms facing each other.",
            "Curl the dumbbells toward your shoulders.",
            "Keep your elbows stationary.",
            "Lower the dumbbells slowly."
        ]
    },


    {
        "id": 16,
        "name": "Push-Ups",
        "type": "Home",
        "muscle": "Triceps + Chest",
        "sets": "3",
        "reps": "10–20",
        "equipment": "Bodyweight",
        "image": img("Pushups"),
        "description": "A classic bodyweight exercise that trains the chest, shoulders and triceps.",
        "steps": [
            "Start in a high plank position.",
            "Keep your body straight.",
            "Lower your chest toward the floor.",
            "Keep your elbows controlled.",
            "Push back to the starting position."
        ]
    },

    {
        "id": 17,
        "name": "Close-Grip Push-Ups",
        "type": "Home",
        "muscle": "Triceps + Chest",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Bodyweight",
        "image": img("Push-Ups_-_Close_Triceps_Position"),
        "description": "A close-hand push-up variation that places greater emphasis on the triceps.",
        "steps": [
            "Start in a push-up position.",
            "Place your hands closer than shoulder width.",
            "Keep your body straight.",
            "Lower your chest toward the floor.",
            "Push yourself back upward."
        ]
    },

    {
        "id": 18,
        "name": "Wide Push-Ups",
        "type": "Home",
        "muscle": "Chest + Triceps",
        "sets": "3",
        "reps": "10–20",
        "equipment": "Bodyweight",
        "image": img("Push-Up_Wide"),
        "description": "A wider push-up variation that trains the chest and supporting arm muscles.",
        "steps": [
            "Start in a high plank.",
            "Place your hands wider than shoulder width.",
            "Keep your body straight.",
            "Lower your chest toward the floor.",
            "Push back to the starting position."
        ]
    },

    {
        "id": 19,
        "name": "Handstand Push-Ups",
        "type": "Home",
        "muscle": "Triceps + Shoulders",
        "sets": "3",
        "reps": "5–10",
        "equipment": "Bodyweight",
        "image": img("Handstand_Push-Ups"),
        "description": "An advanced bodyweight pressing exercise that strongly trains the shoulders and triceps.",
        "steps": [
            "Position yourself upside down against a stable wall.",
            "Place your hands shoulder-width apart.",
            "Brace your core.",
            "Bend your elbows and lower your head.",
            "Press yourself back upward."
        ]
    },

    {
        "id": 20,
        "name": "Push-Ups With Feet Elevated",
        "type": "Home",
        "muscle": "Chest + Triceps",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Bodyweight + Stable Bench",
        "image": img("Push-Ups_With_Feet_Elevated"),
        "description": "An elevated-feet push-up variation that increases the challenge for the upper body.",
        "steps": [
            "Place your feet on a stable elevated surface.",
            "Put your hands on the floor.",
            "Keep your body straight.",
            "Lower your chest toward the floor.",
            "Push yourself back upward."
        ]
    }

]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"


CORE_EXERCISES = [

    # =========================================================
    # GYM EXERCISES
    # =========================================================

    {
        "id": 1,
        "name": "Cable Crunch",
        "type": "Gym",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable Machine",
        "image": img("Cable_Crunch"),
        "description": "A cable-based abdominal exercise that keeps constant resistance on the core.",
        "steps": [
            "Kneel below the high cable pulley.",
            "Hold the rope attachment beside your head.",
            "Keep your hips relatively stationary.",
            "Curl your upper body downward using your abdominal muscles.",
            "Slowly return to the starting position."
        ]
    },

    {
        "id": 2,
        "name": "Cable Reverse Crunch",
        "type": "Gym",
        "muscle": "Lower Abdominals",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable Machine",
        "image": img("Cable_Reverse_Crunch"),
        "description": "A cable resistance exercise that emphasizes the lower abdominal region.",
        "steps": [
            "Lie on your back near the low cable pulley.",
            "Secure your legs to the cable attachment.",
            "Keep your knees bent.",
            "Pull your knees toward your torso using your abs.",
            "Lower your legs slowly."
        ]
    },

    {
        "id": 3,
        "name": "Cable Seated Crunch",
        "type": "Gym",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Cable Machine + Bench",
        "image": img("Cable_Seated_Crunch"),
        "description": "A seated cable crunch that provides continuous resistance to the abdominal muscles.",
        "steps": [
            "Sit on a bench facing away from the cable machine.",
            "Hold the cable rope near your shoulders.",
            "Keep your hips stable.",
            "Curl your torso forward using your abs.",
            "Return slowly to the starting position."
        ]
    },

    {
        "id": 4,
        "name": "Crunches",
        "type": "Gym",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "15–20",
        "equipment": "Bodyweight",
        "image": img("Crunches"),
        "description": "A basic abdominal exercise that develops strength in the front of the core.",
        "steps": [
            "Lie on your back with your knees bent.",
            "Place your hands behind your head.",
            "Keep your feet flat on the floor.",
            "Lift your shoulders toward your knees.",
            "Lower your upper body slowly."
        ]
    },

    {
        "id": 5,
        "name": "Ab Roller",
        "type": "Gym",
        "muscle": "Abdominals + Core",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Ab Wheel",
        "image": img("Ab_Roller"),
        "description": "A challenging core exercise that trains the abdominals and improves trunk stability.",
        "steps": [
            "Kneel on the floor holding the ab wheel.",
            "Place the wheel directly in front of you.",
            "Brace your core tightly.",
            "Roll the wheel forward under control.",
            "Pull the wheel back toward your knees."
        ]
    },

    {
        "id": 6,
        "name": "Decline Crunch",
        "type": "Gym",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Decline Bench",
        "image": img("Decline_Crunch"),
        "description": "A decline abdominal exercise that increases the challenge compared with a standard crunch.",
        "steps": [
            "Lie on the decline bench.",
            "Secure your feet under the pads.",
            "Place your hands behind your head.",
            "Lift your upper body using your abs.",
            "Lower yourself slowly."
        ]
    },

    {
        "id": 7,
        "name": "Russian Twist",
        "type": "Gym",
        "muscle": "Obliques + Abdominals",
        "sets": "3",
        "reps": "12–20 each side",
        "equipment": "Bodyweight or Weight",
        "image": img("Russian_Twist"),
        "description": "A rotational core exercise that targets the obliques and abdominal muscles.",
        "steps": [
            "Sit on the floor with your knees bent.",
            "Lean your torso slightly backward.",
            "Keep your core tight.",
            "Rotate your torso from side to side.",
            "Control each rotation."
        ]
    },

    {
        "id": 8,
        "name": "Hanging Leg Raise",
        "type": "Gym",
        "muscle": "Lower Abdominals + Hip Flexors",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Pull-Up Bar",
        "image": img("Hanging_Leg_Raise"),
        "description": "A hanging core exercise that strongly challenges the lower abdominals and hip flexors.",
        "steps": [
            "Hang from a pull-up bar with your arms extended.",
            "Keep your body controlled.",
            "Raise your legs upward.",
            "Lift until your legs reach a comfortable height.",
            "Lower your legs slowly."
        ]
    },

    {
        "id": 9,
        "name": "3/4 Sit-Up",
        "type": "Gym",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Bodyweight",
        "image": img("3_4_Sit-Up"),
        "description": "A partial sit-up movement that trains the abdominal muscles through controlled trunk flexion.",
        "steps": [
            "Lie on your back with your knees bent.",
            "Place your hands behind your head.",
            "Brace your abdominal muscles.",
            "Raise your upper body toward your knees.",
            "Lower yourself under control."
        ]
    },


    {
        "id": 10,
        "name": "Dead Bug",
        "type": "Home",
        "muscle": "Core + Abdominals",
        "sets": "3",
        "reps": "10–15 each side",
        "equipment": "Bodyweight",
        "image": img("Dead_Bug"),
        "description": "A controlled core exercise that improves abdominal strength and trunk stability.",
        "steps": [
            "Lie on your back with your arms extended upward.",
            "Raise your knees to approximately 90 degrees.",
            "Brace your core against the floor.",
            "Extend one arm and the opposite leg.",
            "Return and alternate sides."
        ]
    },

    {
        "id": 11,
        "name": "Reverse Crunch",
        "type": "Home",
        "muscle": "Lower Abdominals",
        "sets": "3",
        "reps": "12–15",
        "equipment": "Bodyweight",
        "image": img("Reverse_Crunch"),
        "description": "A bodyweight abdominal exercise that emphasizes the lower portion of the core.",
        "steps": [
            "Lie flat on your back.",
            "Raise your legs with your knees bent.",
            "Keep your arms beside your body.",
            "Curl your hips upward toward your chest.",
            "Lower your hips slowly."
        ]
    },

    {
        "id": 12,
        "name": "Alternate Heel Touchers",
        "type": "Home",
        "muscle": "Obliques + Abdominals",
        "sets": "3",
        "reps": "15–20 each side",
        "equipment": "Bodyweight",
        "image": img("Alternate_Heel_Touchers"),
        "description": "A simple floor exercise that targets the abdominal muscles and obliques.",
        "steps": [
            "Lie on your back with your knees bent.",
            "Keep your feet flat on the floor.",
            "Lift your shoulders slightly.",
            "Reach toward your right heel.",
            "Alternate between both sides."
        ]
    },

    {
        "id": 13,
        "name": "Crunch - Hands Overhead",
        "type": "Home",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "12–20",
        "equipment": "Bodyweight",
        "image": img("Crunch_-_Hands_Overhead"),
        "description": "A crunch variation performed with the arms overhead to increase the abdominal challenge.",
        "steps": [
            "Lie flat on your back.",
            "Bend your knees and keep your feet on the floor.",
            "Extend your arms overhead.",
            "Raise your shoulders using your abdominal muscles.",
            "Lower yourself slowly."
        ]
    },

    {
        "id": 14,
        "name": "Flutter Kicks",
        "type": "Home",
        "muscle": "Lower Abdominals + Hip Flexors",
        "sets": "3",
        "reps": "20–30 seconds",
        "equipment": "Bodyweight",
        "image": img("Flutter_Kicks"),
        "description": "A dynamic core exercise that works the lower abdominals and hip flexors.",
        "steps": [
            "Lie on your back.",
            "Keep your legs extended.",
            "Lift your legs slightly from the floor.",
            "Alternate raising each leg.",
            "Keep your core tight throughout the movement."
        ]
    },

    {
        "id": 15,
        "name": "Air Bike",
        "type": "Home",
        "muscle": "Abdominals + Obliques",
        "sets": "3",
        "reps": "15–20 each side",
        "equipment": "Bodyweight",
        "image": img("Air_Bike"),
        "description": "A bicycle-style abdominal movement that trains the core through repeated trunk and leg movement.",
        "steps": [
            "Lie on your back with your hands behind your head.",
            "Raise your shoulders and legs slightly.",
            "Bring one knee toward your chest.",
            "Rotate your torso toward the opposite knee.",
            "Alternate sides continuously."
        ]
    },

    {
        "id": 16,
        "name": "Jackknife Sit-Up",
        "type": "Home",
        "muscle": "Abdominals + Hip Flexors",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Bodyweight",
        "image": img("Jackknife_Sit-Up"),
        "description": "A full-body abdominal movement that combines upper-body and leg movement.",
        "steps": [
            "Lie flat on your back.",
            "Extend your arms and legs.",
            "Brace your core.",
            "Raise your upper body and legs toward each other.",
            "Return slowly to the starting position."
        ]
    },

    {
        "id": 17,
        "name": "Side Bridge",
        "type": "Home",
        "muscle": "Obliques + Core",
        "sets": "3",
        "reps": "20–40 seconds each side",
        "equipment": "Bodyweight",
        "image": img("Side_Bridge"),
        "description": "An isometric core exercise that strongly targets the obliques and improves lateral stability.",
        "steps": [
            "Lie on your side.",
            "Place your elbow underneath your shoulder.",
            "Stack or position your feet comfortably.",
            "Lift your hips from the floor.",
            "Hold the position while keeping your body straight."
        ]
    },

    {
        "id": 18,
        "name": "Toe Touchers",
        "type": "Home",
        "muscle": "Abdominals",
        "sets": "3",
        "reps": "12–20",
        "equipment": "Bodyweight",
        "image": img("Toe_Touchers"),
        "description": "A bodyweight abdominal exercise that emphasizes controlled trunk flexion.",
        "steps": [
            "Lie on your back.",
            "Raise your legs upward.",
            "Extend your arms toward your feet.",
            "Lift your shoulders toward your toes.",
            "Lower your upper body slowly."
        ]
    }

]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"

CARDIO_EXERCISES = [


    {
        "id": 1,
        "name": "Air Bike",
        "type": "Gym",
        "muscle": "Core + Full Body",
        "sets": "3",
        "reps": "30–60 seconds",
        "equipment": "Air Bike",
        "image": img("Air_Bike"),
        "description": "A high-intensity cycling movement that raises the heart rate while training the core and lower body.",
        "steps": [
            "Sit securely on the air bike.",
            "Place your feet on the pedals and grip the handles.",
            "Push and pull the handles while pedaling.",
            "Maintain a strong and controlled pace.",
            "Continue for the prescribed time."
        ]
    },

    {
        "id": 2,
        "name": "Battling Ropes",
        "type": "Gym",
        "muscle": "Full Body + Shoulders",
        "sets": "3",
        "reps": "30–45 seconds",
        "equipment": "Battle Ropes",
        "image": img("Battling_Ropes"),
        "description": "A high-intensity conditioning exercise using alternating rope waves to increase cardiovascular endurance.",
        "steps": [
            "Stand facing the anchor point with one rope in each hand.",
            "Keep your knees slightly bent and brace your core.",
            "Raise one arm while lowering the other.",
            "Continue alternating your arms rapidly.",
            "Maintain the rope waves for the prescribed time."
        ]
    },

    {
        "id": 3,
        "name": "Bicycling",
        "type": "Gym",
        "muscle": "Quadriceps + Hamstrings",
        "sets": "1–3",
        "reps": "10–30 minutes",
        "equipment": "Bicycle",
        "image": img("Bicycling"),
        "description": "A cycling exercise that develops cardiovascular endurance while working the major muscles of the legs.",
        "steps": [
            "Adjust the bicycle seat to a comfortable height.",
            "Place your feet securely on the pedals.",
            "Start pedaling at an easy pace.",
            "Gradually increase your speed or resistance.",
            "Maintain a steady pace for the workout duration."
        ]
    },

    {
        "id": 4,
        "name": "Bicycling, Stationary",
        "type": "Gym",
        "muscle": "Quadriceps + Hamstrings",
        "sets": "1–3",
        "reps": "10–30 minutes",
        "equipment": "Stationary Bike",
        "image": img("Bicycling_Stationary"),
        "description": "A low-impact stationary cycling workout designed to improve cardiovascular fitness and leg endurance.",
        "steps": [
            "Sit on the stationary bike.",
            "Adjust the seat to your height.",
            "Place your feet securely on the pedals.",
            "Begin pedaling at a comfortable pace.",
            "Increase resistance gradually if required."
        ]
    },

    {
        "id": 5,
        "name": "Jogging, Treadmill",
        "type": "Gym",
        "muscle": "Quadriceps + Glutes",
        "sets": "1–3",
        "reps": "10–30 minutes",
        "equipment": "Treadmill",
        "image": img("Jogging_Treadmill"),
        "description": "A treadmill-based cardiovascular exercise that improves endurance while training the lower body.",
        "steps": [
            "Step onto the treadmill carefully.",
            "Select a comfortable jogging speed.",
            "Keep your posture upright.",
            "Jog naturally without holding the rails.",
            "Maintain your pace for the planned duration."
        ]
    },

    {
        "id": 6,
        "name": "Prowler Sprint",
        "type": "Gym",
        "muscle": "Legs + Full Body",
        "sets": "3–5",
        "reps": "15–30 seconds",
        "equipment": "Prowler Sled",
        "image": img("Prowler_Sprint"),
        "description": "A high-intensity sled sprint that develops cardiovascular conditioning and lower-body power.",
        "steps": [
            "Load the prowler with an appropriate weight.",
            "Grip the handles firmly.",
            "Lean your body forward while keeping your back controlled.",
            "Drive through the ground using short powerful steps.",
            "Push the sled for the prescribed distance."
        ]
    },

    {
        "id": 7,
        "name": "Recumbent Bike",
        "type": "Gym",
        "muscle": "Quadriceps + Hamstrings",
        "sets": "1–3",
        "reps": "10–30 minutes",
        "equipment": "Recumbent Bike",
        "image": img("Recumbent_Bike"),
        "description": "A seated cycling exercise that provides cardiovascular training with relatively low impact on the joints.",
        "steps": [
            "Sit comfortably in the recumbent bike.",
            "Adjust the seat so your legs can pedal comfortably.",
            "Place your feet on the pedals.",
            "Begin pedaling at a steady pace.",
            "Increase resistance gradually if required."
        ]
    },


    {
        "id": 8,
        "name": "Bench Jump",
        "type": "Home",
        "muscle": "Quadriceps + Glutes",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Stable Bench",
        "image": img("Bench_Jump"),
        "description": "An explosive jumping exercise that raises the heart rate while developing lower-body power.",
        "steps": [
            "Stand facing a stable bench.",
            "Bend your knees slightly.",
            "Swing your arms and jump onto the bench.",
            "Land softly with both feet.",
            "Step down carefully and repeat."
        ]
    },

    {
        "id": 9,
        "name": "Fast Skipping",
        "type": "Home",
        "muscle": "Calves + Quadriceps",
        "sets": "3",
        "reps": "30–60 seconds",
        "equipment": "Bodyweight",
        "image": img("Fast_Skipping"),
        "description": "A fast skipping movement that improves foot speed, coordination and cardiovascular conditioning.",
        "steps": [
            "Stand upright with one foot slightly forward.",
            "Begin a step-hop pattern.",
            "Alternate your feet quickly.",
            "Keep your movements light and controlled.",
            "Continue at a fast pace for the prescribed time."
        ]
    },

    {
        "id": 10,
        "name": "Hurdle Hops",
        "type": "Home",
        "muscle": "Quadriceps + Calves",
        "sets": "3",
        "reps": "8–15",
        "equipment": "Small Hurdles",
        "image": img("Hurdle_Hops"),
        "description": "A plyometric exercise that improves explosive leg power, agility and cardiovascular conditioning.",
        "steps": [
            "Place small hurdles or safe obstacles in a row.",
            "Stand facing the first hurdle.",
            "Jump over it using both feet.",
            "Land softly with bent knees.",
            "Immediately jump over the next hurdle."
        ]
    },

    {
        "id": 11,
        "name": "Mountain Climbers",
        "type": "Home",
        "muscle": "Core + Quadriceps",
        "sets": "3",
        "reps": "20–30 seconds",
        "equipment": "Bodyweight",
        "image": img("Mountain_Climbers"),
        "description": "A dynamic full-body cardio exercise that increases heart rate while training the core and legs.",
        "steps": [
            "Start in a high plank position.",
            "Keep your body straight and core tight.",
            "Drive one knee toward your chest.",
            "Return the leg and bring the opposite knee forward.",
            "Continue alternating quickly."
        ]
    },

    {
        "id": 12,
        "name": "Quick Leap",
        "type": "Home",
        "muscle": "Quadriceps + Calves",
        "sets": "3",
        "reps": "8–12",
        "equipment": "Stable Box",
        "image": img("Quick_Leap"),
        "description": "An explosive jumping exercise that develops lower-body power and elevates cardiovascular intensity.",
        "steps": [
            "Stand approximately one to two feet from a stable box.",
            "Bend slightly and prepare to jump.",
            "Jump onto the box using your hips and legs.",
            "Land with both feet and bent knees.",
            "Stand tall and repeat the movement."
        ]
    },

    {
        "id": 13,
        "name": "Rocket Jump",
        "type": "Home",
        "muscle": "Quadriceps + Calves",
        "sets": "3",
        "reps": "10–15",
        "equipment": "Bodyweight",
        "image": img("Rocket_Jump"),
        "description": "An explosive bodyweight jump that increases heart rate while developing lower-body power.",
        "steps": [
            "Stand with your feet around shoulder-width apart.",
            "Lower into a partial squat.",
            "Explode upward as high as comfortably possible.",
            "Extend your body fully during the jump.",
            "Land softly and absorb the impact."
        ]
    },

    {
        "id": 14,
        "name": "Single-Cone Sprint Drill",
        "type": "Home",
        "muscle": "Quadriceps + Hamstrings",
        "sets": "3",
        "reps": "20–30 seconds",
        "equipment": "Cone",
        "image": img("Single-Cone_Sprint_Drill"),
        "description": "A fast footwork drill that improves agility, speed and cardiovascular conditioning.",
        "steps": [
            "Place a cone on the floor.",
            "Stand beside the cone in an athletic stance.",
            "Move your feet rapidly while staying light on your toes.",
            "Circle around the cone quickly.",
            "Rest and repeat for the next set."
        ]
    }

]

IMAGE_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

def img(folder):
    return IMAGE_BASE + folder + "/0.jpg"

FULLBODY_EXERCISES = [



{
    "id": 1,
    "name": "Barbell Deadlift",
    "type": "Gym",
    "muscle": "Back + Glutes + Hamstrings + Core",
    "sets": "3–4",
    "reps": "6–10",
    "equipment": "Barbell",
    "image": img("Barbell_Deadlift"),
    "description": "A major compound exercise that trains the posterior chain, grip, core and lower body.",
    "steps": [
        "Stand with your feet about hip-width apart and the bar over your mid-foot.",
        "Bend your hips and knees and grip the bar.",
        "Brace your core and keep your back neutral.",
        "Drive through your feet while extending your hips and knees.",
        "Stand tall and lower the bar under control."
    ]
},

{
    "id": 2,
    "name": "Barbell Full Squat",
    "type": "Gym",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3–4",
    "reps": "8–12",
    "equipment": "Barbell + Rack",
    "image": img("Barbell_Full_Squat"),
    "description": "A compound lower-body movement that also requires strong core and upper-body stabilization.",
    "steps": [
        "Place the barbell securely across your upper back.",
        "Stand with your feet at a comfortable width.",
        "Brace your core and keep your chest up.",
        "Lower your hips by bending your knees and hips.",
        "Drive through your feet to return to standing."
    ]
},

{
    "id": 3,
    "name": "Dumbbell Lunges",
    "type": "Gym",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "8–12 each leg",
    "equipment": "Dumbbells",
    "image": img("Dumbbell_Lunges"),
    "description": "A unilateral compound movement that trains the legs while challenging balance and core stability.",
    "steps": [
        "Stand upright holding a dumbbell in each hand.",
        "Step forward with one leg.",
        "Lower your body until both knees are comfortably bent.",
        "Keep your torso upright and core braced.",
        "Push through your front foot and return."
    ]
},

{
    "id": 4,
    "name": "Power Clean",
    "type": "Gym",
    "muscle": "Full Body + Traps + Legs",
    "sets": "3–4",
    "reps": "3–6",
    "equipment": "Barbell",
    "image": img("Power_Clean"),
    "description": "An explosive compound exercise involving the legs, hips, back, shoulders and arms.",
    "steps": [
        "Stand behind the bar with your feet about hip-width apart.",
        "Grip the bar and keep your back neutral.",
        "Drive through your legs and extend your hips explosively.",
        "Pull the bar upward and catch it at shoulder height.",
        "Lower the bar safely and repeat."
    ]
},

{
    "id": 5,
    "name": "Push Press",
    "type": "Gym",
    "muscle": "Shoulders + Legs + Triceps + Core",
    "sets": "3",
    "reps": "6–10",
    "equipment": "Barbell",
    "image": img("Push_Press"),
    "description": "A powerful overhead movement that combines leg drive with upper-body pressing.",
    "steps": [
        "Position the barbell at shoulder height.",
        "Stand with your feet around shoulder-width apart.",
        "Brace your core and slightly bend your knees.",
        "Drive upward with your legs while pressing the bar overhead.",
        "Lower the bar back to your shoulders under control."
    ]
},

{
    "id": 6,
    "name": "Dumbbell Squat",
    "type": "Gym",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "10–12",
    "equipment": "Dumbbells",
    "image": img("Dumbbell_Squat"),
    "description": "A compound squat variation that trains the lower body while requiring core stabilization.",
    "steps": [
        "Hold a dumbbell in each hand at your sides.",
        "Stand with your feet around shoulder-width apart.",
        "Brace your core and keep your chest up.",
        "Lower into a controlled squat.",
        "Drive through your feet to stand."
    ]
},

{
    "id": 7,
    "name": "Dumbbell Step Ups",
    "type": "Gym",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "8–12 each leg",
    "equipment": "Dumbbells + Bench",
    "image": img("Dumbbell_Step_Ups"),
    "description": "A unilateral full-body-supporting movement that develops leg strength, balance and stability.",
    "steps": [
        "Hold a dumbbell in each hand.",
        "Stand in front of a stable platform.",
        "Place one foot firmly on the platform.",
        "Push through that foot and step upward.",
        "Step down under control and switch legs."
    ]
},

{
    "id": 8,
    "name": "Pullups",
    "type": "Gym",
    "muscle": "Back + Biceps + Core",
    "sets": "3",
    "reps": "6–12",
    "equipment": "Pull-Up Bar",
    "image": img("Pullups"),
    "description": "A compound bodyweight exercise that develops the back, arms and core.",
    "steps": [
        "Grip the pull-up bar with your hands slightly wider than shoulder width.",
        "Hang with your arms extended.",
        "Brace your core and pull your chest toward the bar.",
        "Drive your elbows down and back.",
        "Lower yourself slowly to the starting position."
    ]
},

{
    "id": 9,
    "name": "Plie Dumbbell Squat",
    "type": "Gym",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "10–15",
    "equipment": "Dumbbell",
    "image": img("Plie_Dumbbell_Squat"),
    "description": "A wide-stance squat variation that trains the lower body while requiring core stability.",
    "steps": [
        "Hold a dumbbell with both hands.",
        "Stand with your feet wider than shoulder width.",
        "Point your toes slightly outward.",
        "Lower your hips while keeping your chest up.",
        "Push through your heels to return to standing."
    ]
},

{
    "id": 10,
    "name": "Alternating Renegade Row",
    "type": "Gym",
    "muscle": "Back + Core + Shoulders + Arms",
    "sets": "3",
    "reps": "8–12 each arm",
    "equipment": "Kettlebells",
    "image": img("Alternating_Renegade_Row"),
    "description": "A demanding compound exercise combining a plank position with alternating rows.",
    "steps": [
        "Place two kettlebells on the floor.",
        "Start in a strong plank position holding the kettlebells.",
        "Brace your core and keep your hips stable.",
        "Row one kettlebell toward your side.",
        "Lower it and repeat with the opposite arm."
    ]
},


{
    "id": 11,
    "name": "Bodyweight Squat",
    "type": "Home",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "15–20",
    "equipment": "Bodyweight",
    "image": img("Bodyweight_Squat"),
    "description": "A basic compound movement for developing lower-body strength and core stability.",
    "steps": [
        "Stand with your feet around shoulder-width apart.",
        "Keep your chest up and core tight.",
        "Push your hips backward.",
        "Bend your knees and lower your body.",
        "Drive through your feet to stand."
    ]
},

{
    "id": 12,
    "name": "Bodyweight Walking Lunge",
    "type": "Home",
    "muscle": "Quadriceps + Glutes + Hamstrings + Core",
    "sets": "3",
    "reps": "10–15 each leg",
    "equipment": "Bodyweight",
    "image": img("Bodyweight_Walking_Lunge"),
    "description": "A dynamic lower-body exercise that challenges balance, coordination and core stability.",
    "steps": [
        "Stand upright with your feet together.",
        "Step forward with one leg.",
        "Lower your hips into a lunge.",
        "Push through the front foot.",
        "Continue walking while alternating legs."
    ]
},

{
    "id": 13,
    "name": "Mountain Climbers",
    "type": "Home",
    "muscle": "Core + Shoulders + Legs",
    "sets": "3",
    "reps": "20–30",
    "equipment": "Bodyweight",
    "image": img("Mountain_Climbers"),
    "description": "A dynamic bodyweight exercise that combines core stability with rapid leg movement.",
    "steps": [
        "Start in a high plank position.",
        "Keep your body in a straight line.",
        "Drive one knee toward your chest.",
        "Return the leg and bring the opposite knee forward.",
        "Continue alternating at a controlled pace."
    ]
},

{
    "id": 14,
    "name": "Air Bike",
    "type": "Home",
    "muscle": "Core + Hip Flexors + Legs",
    "sets": "3",
    "reps": "15–20 each side",
    "equipment": "Bodyweight",
    "image": img("Air_Bike"),
    "description": "A dynamic core exercise combining trunk rotation with alternating leg movement.",
    "steps": [
        "Lie flat on your back.",
        "Place your hands beside your head.",
        "Raise your shoulders and legs from the floor.",
        "Bring one elbow toward the opposite knee.",
        "Alternate sides in a controlled cycling motion."
    ]
},

{
    "id": 15,
    "name": "Ab Roller",
    "type": "Home",
    "muscle": "Core + Shoulders + Arms",
    "sets": "3",
    "reps": "8–15",
    "equipment": "Ab Wheel",
    "image": img("Ab_Roller"),
    "description": "A challenging compound core movement requiring strong abdominal and upper-body stabilization.",
    "steps": [
        "Kneel on the floor holding the ab wheel.",
        "Place the wheel directly in front of you.",
        "Brace your core tightly.",
        "Slowly roll forward while keeping your body controlled.",
        "Pull the wheel back toward your knees."
    ]
},

{
    "id": 16,
    "name": "Sledgehammer Swings",
    "type": "Home",
    "muscle": "Full Body + Core + Shoulders + Legs",
    "sets": "3",
    "reps": "10–15 each side",
    "equipment": "Sledgehammer + Tire",
    "image": img("Sledgehammer_Swings"),
    "description": "An explosive movement that combines hip rotation, core strength, shoulders and legs.",
    "steps": [
        "Stand beside a stable tire with a staggered stance.",
        "Grip the sledgehammer with both hands.",
        "Raise the hammer over your shoulder.",
        "Rotate your hips and swing the hammer toward the tire.",
        "Control the rebound and repeat."
    ]
},

{
    "id": 17,
    "name": "Medicine Ball Scoop Throw",
    "type": "Home",
    "muscle": "Full Body + Legs + Core + Shoulders",
    "sets": "3",
    "reps": "8–12",
    "equipment": "Medicine Ball",
    "image": img("Medicine_Ball_Scoop_Throw"),
    "description": "An explosive full-body movement using the legs, hips and upper body to generate power.",
    "steps": [
        "Hold the medicine ball with both hands.",
        "Stand with your feet in a stable stance.",
        "Lower into a partial squat.",
        "Drive through your legs and hips.",
        "Explosively throw the ball upward and forward."
    ]
},

{
    "id": 18,
    "name": "Standing Long Jump",
    "type": "Home",
    "muscle": "Legs + Glutes + Core",
    "sets": "3",
    "reps": "6–10",
    "equipment": "Bodyweight",
    "image": img("Standing_Long_Jump"),
    "description": "An explosive lower-body movement that develops power, coordination and full-body stability.",
    "steps": [
        "Stand with your feet around shoulder-width apart.",
        "Bend your knees and swing your arms backward.",
        "Drive your hips and legs forward explosively.",
        "Jump forward as far as comfortably possible.",
        "Land softly and regain your balance."
    ]
},

{
    "id": 19,
    "name": "Clean and Press",
    "type": "Gym",
    "muscle": "Full Body + Shoulders + Legs + Core",
    "sets": "3",
    "reps": "6–10",
    "equipment": "Barbell",
    "image": img("Clean_and_Press"),
    "description": "A compound Olympic-style movement combining a barbell clean with an overhead press.",
    "steps": [
        "Stand behind the barbell with a shoulder-width stance.",
        "Grip the bar and keep your back neutral.",
        "Drive through your legs and hips to bring the bar to your shoulders.",
        "Stabilize the bar at shoulder height.",
        "Press the bar overhead and lower it safely."
    ]
},

{
    "id": 20,
    "name": "Push-Ups",
    "type": "Home",
    "muscle": "Chest + Shoulders + Triceps + Core",
    "sets": "3",
    "reps": "10–20",
    "equipment": "Bodyweight",
    "image": img("Pushups"),
    "description": "A bodyweight compound movement that trains the upper body while requiring full-body core stability.",
    "steps": [
        "Start in a high plank position.",
        "Keep your body straight from head to heels.",
        "Lower your chest toward the floor.",
        "Keep your elbows controlled.",
        "Push through your hands to return to the starting position."
    ]
}

]

BLOG_POSTS = [
    {
        "slug": "5-compound-lifts-every-beginner-should-master",
        "title": "5 Compound Lifts Every Beginner Should Master",
        "excerpt": "Build a rock-solid foundation with these five essential movements before chasing isolation work.",
        "content": "Compound lifts recruit multiple muscle groups at once, making them the most efficient way to build strength as a beginner. Start with the squat, deadlift, bench press, overhead press, and barbell row. Focus on form before adding weight — record yourself and compare to reference videos. Progressive overload on these five lifts alone will carry a beginner through their first year of training more effectively than any isolation-heavy routine.",
        "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=1200&auto=format&fit=crop", "category": "Training",
        "category": "Training",
        "author": "Coach Rahul",
        "date": "July 10, 2026",
        "read_time": "6 min read",
    },
    {
        "slug": "high-protein-meals-for-muscle-recovery",
        "title": "High-Protein Meals for Muscle Recovery",
        "excerpt": "Simple, affordable meals to help you hit your protein targets without spending hours in the kitchen.",
        "content": "Muscle protein synthesis peaks in the hours after training, making post-workout nutrition critical. Aim for 25-40g of protein per meal from sources like eggs, paneer, chicken, lentils, and Greek yogurt. Pair protein with a moderate carb source to replenish glycogen. Meal prepping on Sundays can save significant time during the week.",
        "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1200&auto=format&fit=crop", "category": "Nutrition",
        "category": "Nutrition",
        "author": "Coach Meera",
        "date": "July 5, 2026",
        "read_time": "4 min read",
    },
    {
        "slug": "beginner-cardio-that-doesnt-kill-your-gains",
        "title": "Beginner Cardio That Doesn't Kill Your Gains",
        "excerpt": "How to add conditioning work without sabotaging your strength progress.",
        "content": "Excessive cardio can interfere with strength and hypertrophy goals if not programmed correctly. Stick to 2-3 sessions of low-intensity steady state (LISS) or short HIIT intervals per week, ideally separated from heavy lifting days. Walking, cycling, and rowing are joint-friendly options that support recovery rather than compete with it.",
        "img": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=1200&auto=format&fit=crop", "category": "Cardio",
        "category": "Cardio",
        "author": "Coach Arjun",
        "date": "June 28, 2026",
        "read_time": "5 min read",
    },
    {
        "slug": "why-sleep-is-your-most-underrated-recovery-tool",
        "title": "Why Sleep Is Your Most Underrated Recovery Tool",
        "excerpt": "You can nail every rep in the gym, but poor sleep will quietly undo your progress.",
        "content": "Growth hormone release peaks during deep sleep, making it one of the most powerful (and free) recovery tools available. Aim for 7-9 hours per night, keep a consistent sleep schedule, and avoid screens 30-60 minutes before bed. Athletes who sleep less than 6 hours regularly show measurably slower strength gains and higher injury rates. Treat sleep as part of your training program, not an afterthought.",
        "img": "https://images.unsplash.com/photo-1522898467493-49726bf28798?q=80&w=1200&auto=format&fit=crop",
        "category": "Recovery",
        "author": "Coach Priya",
        "date": "July 15, 2026",
        "read_time": "5 min read",
    },
    {
        "slug": "building-mental-discipline-for-consistent-training",
        "title": "Building Mental Discipline for Consistent Training",
        "excerpt": "Motivation fades — here's how to build the discipline that keeps you showing up anyway.",
        "content": "Relying on motivation alone is unsustainable; the athletes who succeed long-term build systems instead. Set a fixed training schedule and treat it as non-negotiable, like a work meeting. Track small wins to build momentum, and separate your identity ('I am someone who trains') from daily mood swings. Discipline is a skill you strengthen through repetition, not a trait you either have or don't.",
        "img": "https://images.unsplash.com/photo-1601422407692-ec4eeec1d9b3?q=80&w=1200&auto=format&fit=crop",
        "category": "Mindset",
        "author": "Coach Arjun",
        "date": "July 18, 2026",
        "read_time": "4 min read",
    },
]
