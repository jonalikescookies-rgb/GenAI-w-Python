from google import genai
client=genai.Client(api_key="AIzaSyDbYT_dMpPWJTkS9Rl89oL_KjsHIVhl2Z4")
response= client.models.generate_content(
    model="gemini-2.5-flash",
    contents="hello")

print(response.text)
