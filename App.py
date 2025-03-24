import streamlit as st # type: ignore
import requests # type: ignore

# Streamlit App Title
st.title("AI-Powered Car Price Predictions for the Modern Driver")

# Add car image to sidebar
car_image_path = "car_image.png"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image(car_image_path, use_container_width=True)
except FileNotFoundError:
    st.sidebar.warning("Car image file not found. Please check the file path.")
    
# Add new car pic to sidebar
car_image_path = "car_pic.png"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image(car_image_path, use_container_width=True)
except FileNotFoundError:
    st.sidebar.warning("Car image file not found. Please check the file path.")

st.sidebar.title("Developer: Abhishek Kumar")

# Add my jpg to sidebar
car_image_path = "pic.jpg"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image("pic.jpg", use_container_width=True)
except FileNotFoundError:
    st.sidebar.warning("pic.jpg. Please check the file path.")



# User Input Section
st.header("Welcome to the Car Recommendation System")
user_name = st.text_input("Enter your name:")
phone_number = st.text_input("Enter your phone number:")

if user_name and phone_number:
    st.success(f"Hello, {user_name}! Let's find the perfect car for you.")

    # Input Section
st.header("Find Your Perfect Car")
user_budget = st.number_input(
    "Enter your budget (in INR):",
    min_value=100000,
    max_value=100000000,
    step=50000,
    value=None  # Removes pre-filled value
)

# Show a lovely message after budget input
car_type = st.selectbox(
    "Select car type:",
    ["SUV", "Electric", "Hatchback", "Luxury", "Sedan", "Convertible"]
)
if user_budget:
    st.subheader("Thank You!")
    st.write(
        f"Dear {user_name}, thank you for providing your budget of INR {user_budget:,}. "
        "We understand how important it is to find the right car within your price range. "
        "Our system will recommend the best cars that meet your expectations. "
        "Stay tuned for amazing options tailored just for you. Let’s make your car search effortless and enjoyable!"
    )


    # Mock car data (20 cars, price up to 10 crore)
    def fetch_car_data():
            sample_data = [
                {"name": "Toyota Fortuner", "type": "SUV", "price": 3200000, "details": "The Toyota Fortuner is a rugged SUV known for its off-road capability, spacious interior, and powerful diesel engine. It comes with advanced safety features and modern infotainment."},
                {"name": "Hyundai Creta", "type": "SUV", "price": 1800000, "details": "The Hyundai Creta is a popular compact SUV with a stylish design, comfortable cabin, and efficient engine options. It is equipped with a touchscreen infotainment system and connected car features."},
                {"name": "Tesla Model 3", "type": "Electric", "price": 4500000, "details": "Tesla Model 3 is a premium electric sedan offering excellent range, cutting-edge autopilot features, and a minimalist interior design. It is one of the most affordable Tesla models."},
                {"name": "Maruti Swift", "type": "Hatchback", "price": 800000, "details": "Maruti Swift is a compact hatchback known for its fuel efficiency, sporty look, and reliable performance. It is an ideal car for city driving and offers a smooth ride."},
                {"name": "BMW 5 Series", "type": "Luxury", "price": 6500000, "details": "The BMW 5 Series is a luxury sedan combining elegant design with powerful performance. It features advanced driver assistance systems and a luxurious interior."},
                {"name": "Mercedes-Benz G-Class", "type": "Luxury", "price": 100000000, "details": "The Mercedes-Benz G-Class is an iconic luxury SUV with unmatched off-road capability, a powerful engine, and a plush interior with premium materials."},
                {"name": "Audi Q7", "type": "SUV", "price": 8900000, "details": "The Audi Q7 is a luxurious SUV offering a blend of style, performance, and advanced technology. It features a spacious interior and a powerful engine."},
                {"name": "Honda City", "type": "Sedan", "price": 1500000, "details": "Honda City is a reliable sedan known for its fuel efficiency, comfortable interior, and smooth performance. It comes with modern features and a stylish design."},
                {"name": "Ford Mustang", "type": "Convertible", "price": 7400000, "details": "The Ford Mustang is an iconic convertible with a powerful V8 engine, aggressive styling, and thrilling performance. It is a symbol of American muscle cars."},
                {"name": "Jaguar F-Type", "type": "Convertible", "price": 9500000, "details": "The Jaguar F-Type is a luxury sports convertible with a sleek design, powerful engine options, and a driver-focused cockpit. It delivers an exhilarating driving experience."},
                {"name": "Mahindra Thar", "type": "SUV", "price": 1600000, "details": "The Mahindra Thar is a rugged SUV designed for off-road enthusiasts. It features a robust build, advanced 4x4 system, and a modern cabin with essential comforts."},
                {"name": "Kia Seltos", "type": "SUV", "price": 2000000, "details": "The Kia Seltos is a compact SUV with a bold design, feature-rich interior, and efficient engine options. It is known for its connected car technology."},
                {"name": "Porsche 911", "type": "Luxury", "price": 120000000, "details": "The Porsche 911 is a high-performance sports car with timeless design, powerful engines, and exceptional handling. It is a true icon in the automotive world."},
                {"name": "Tata Nexon EV", "type": "Electric", "price": 1700000, "details": "The Tata Nexon EV is an affordable electric SUV with a decent range, modern features, and a stylish design. It is ideal for eco-conscious buyers."},
                {"name": "Nissan Magnite", "type": "Hatchback", "price": 900000, "details": "The Nissan Magnite is a budget-friendly compact SUV with a bold design, spacious cabin, and efficient performance. It offers great value for money."},
                {"name": "Ferrari Roma", "type": "Luxury", "price": 220000000, "details": "The Ferrari Roma is a sleek grand tourer with a powerful V8 engine, elegant design, and cutting-edge technology. It embodies Italian automotive excellence."},
                {"name": "Lamborghini Huracan", "type": "Luxury", "price": 340000000, "details": "The Lamborghini Huracan is a supercar with a striking design, powerful V10 engine, and track-level performance. It is a dream car for enthusiasts."},
                {"name": "Volvo XC90", "type": "SUV", "price": 8000000, "details": "The Volvo XC90 is a premium SUV with a focus on safety, luxury, and sustainability. It features a hybrid option and a spacious interior."},
                {"name": "Skoda Superb", "type": "Sedan", "price": 3200000, "details": "The Skoda Superb is a premium sedan with a spacious cabin, refined performance, and modern features. It is a perfect blend of comfort and style."},
                {"name": "Rolls-Royce Phantom", "type": "Luxury", "price": 950000000, "details": "The Rolls-Royce Phantom is the pinnacle of luxury, offering unmatched comfort, bespoke design, and a smooth, powerful V12 engine."}
            ]
            return sample_data

        # Recommendation Logic
    def recommend_cars(budget, car_type):
            cars = fetch_car_data()
            filtered_cars = [car for car in cars if car["type"] == car_type and car["price"] <= budget]
            return filtered_cars

        # Generate recommendations
    if st.button("Show Recommendations"):
            recommendations = recommend_cars(user_budget, car_type)
            if recommendations:
                st.subheader("Recommended Cars:")
                for car in recommendations:
                    st.write(f"- *{car['name']}*: INR {car['price']:,}")
            else:
                st.warning("No cars found matching your criteria. Try increasing your budget or changing the car type.")

    # Car Details Section
    st.header("Get Car Details")
    car_name = st.text_input("Enter car name for details:")
    if st.button("Get Details"):
            if car_name:
                cars = fetch_car_data()
                car_details = next((car for car in cars if car["name"].lower() == car_name.lower()), None)
                if car_details:
                    st.success(f"Details for {car_name}:\n\n{car_details['details']}\n\n")
                    st.info(
                        "This car is a perfect blend of style, performance, and features. It offers exceptional value in its segment. "
                        "Known for its reliability and comfort, this car also comes equipped with advanced safety features. "
                        "With a spacious interior and modern design, it is well-suited for families and professionals alike. "
                        "The engine delivers robust performance, making it an ideal choice for both city driving and long-distance travel. "
                        "It includes a user-friendly infotainment system and multiple connectivity options for a seamless experience. "
                        "Additionally, the car boasts impressive fuel efficiency, ensuring cost-effective ownership. "
                        "Its stylish exterior design turns heads on the road, while the premium interior materials enhance the luxury feel."
                    )
