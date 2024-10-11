# from library.libraries import *


# opencage_key = "19cbd4c87181428398cdb8690b439ebd"

# def get_lat_long(number_location):
#     geocoder = OpenCageGeocode(opencage_key)
#     results = geocoder.geocode(number_location)

#     if results:
#         lat = results[0]['geometry']['lat']
#         lng = results[0]['geometry']['lng']
#         return lat, lng
#     else:
#         print(Fore.RED + "No results found for the location.")
#         return None, None

# def get_phone_info(phone_number):
#     print(" ")
#     print(Fore.YELLOW + Style.BRIGHT + "Gathering _Phone_Information...", end="")
#     for _ in range(5):
#         print(Fore.GREEN + ".", end="")
#         sys.stdout.flush()
#         time.sleep(1)
#     # Replace 'YOUR_API_KEY' with your actual NumVerify API key
#     api_key = 'bc1331634ac062e733664492ac2eb6b3'

#     url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'
    
#     try:
#         response = requests.get(url)
#         data = response.json()
        
#         # Check if the response is valid
#         if not data.get('valid'):
#             print(Fore.RED + "The phone number is not valid.")
#             return None
        
#         # Extract relevant information
#         country_name = data.get('country_name', 'N/A')
#         country_code = data.get('country_code', 'N/A')
#         local_format = data.get('local_format', 'N/A')
#         international_format = data.get('international_format', 'N/A')
#         carrier_name = data.get('carrier', 'N/A')
#         line_type = data.get('line_type', 'N/A')
        
#         # Get location for latitude and longitude
#         check_number = phonenumbers.parse(phone_number)
#         number_location = geocoder.description_for_number(check_number, "en")
#         lat, lng = get_lat_long(number_location)

#         # Print the details of the phone number in colored output
#         print(Fore.YELLOW + Style.BRIGHT + f"\nPhone Number Information:")
#         print(Fore.YELLOW + f"Country Name: {Fore.CYAN + country_name}")
#         print(Fore.YELLOW + f"Country Code: {Fore.CYAN + country_code}")
#         print(Fore.YELLOW + f"Local Format: {Fore.CYAN + local_format}")
#         print(Fore.YELLOW + f"International Format: {Fore.CYAN + international_format}")
#         print(Fore.YELLOW + f"Carrier: {Fore.CYAN + carrier_name}")
#         print(Fore.YELLOW + f"Line Type: {Fore.CYAN + line_type}")
#         print(Fore.YELLOW + f"Latitude: {Fore.CYAN + str(lat) if lat else 'N/A'}")
#         print(Fore.YELLOW + f"Longitude: {Fore.CYAN + str(lng) if lng else 'N/A'}")

#         # Create a map if latitude and longitude are available
#         if lat is not None and lng is not None:
#             map_location = folium.Map(location=[lat, lng], zoom_start=9)
#             folium.Marker([lat, lng], popup=number_location).add_to(map_location)
#             map_location.save("mylocation.html")
#             print(Fore.GREEN + "Map has been saved as 'mylocation.html'.")

#         return {
#             "Country Name": country_name,
#             "Country Code": country_code,
#             "Local Format": local_format,
#             "International Format": international_format,
#             "Carrier": carrier_name,
#             "Line Type": line_type,
#             "Latitude": lat,
#             "Longitude": lng
#         }

#     except Exception as e:
#         print(Fore.RED + f"Error occurred: {e}")
#         return None
