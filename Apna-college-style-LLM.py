from google import genai

client = genai.Client(api_key="AIzaSyAzZ1DdF9s6tM9i4ty0c7kBMmkVGmsQiTY")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="what is apna college"
)
print(response.text)
exmples = """
The Apna College YouTube channel is a popular Indian educational platform led by Shradha Khapra, a former Microsoft software engineer and DRDO intern. The channel focuses on coding tutorials, placement preparation, and career guidance,
aiming to make tech education accessible to students across India.
You are a helpful and knowledgeable chatbot. Answer user questions clearly and accurately. 
User: What's the capital of France?
Bot: The capital of France is Paris.

User: How many continents are there?
Bot: There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia.

Now continue the conversation:
"""