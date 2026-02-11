print("..< Weather Advisory System >...")

temperature = float(input("Enter temperature (°C): "))
weather = input("Enter weather condition (sunny / rainy / cloudy): ").lower()
wind_speed = int(input("Enter wind speed (km/h): "))

print("\n--- Weather Advisory ---")

# Temperature based conditions
if temperature < 10:
    print(" Cold Weather: Wear warm clothes.")
elif temperature >= 10 and temperature < 25:
    print(" Pleasant Weather: Enjoy your day.")
else:
    print(" Hot Weather: Stay hydrated and avoid sunlight.")


if weather == "rainy":
    print("Carry an umbrella.")
elif weather == "sunny":
    print(" Use sunscreen and sunglasses.")
elif weather == "cloudy":
    print(" Weather looks cloudy, be prepared.")
else:
    print(" Unknown weather condition.")


if wind_speed > 40:
    print("💨 Strong wind alert! Avoid outdoor activities.")
else:
    print("🍃 Wind conditions are normal.")

print("\n---- Stay Safe & Updated ----")
