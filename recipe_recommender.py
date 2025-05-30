from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GOOGLE_API_KEY")
if not api:
    print("Error in Google api key...")

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    google_api_key = api
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=(
        "You are a recipe recommender chatbot. Only recommend recipes based on the user input.\n"
        "Avoid using symbols like * or **.\n"
        "Do not give any response other than dish recommendations and a short greeting.\n"
        "Make sure your response is at least 50 words long.\n\n"
        "User input: {user_input}"
    )
)

query = input("Enter input: ").strip()

if query:
    response = llm.invoke(prompt.format(user_input = query))
    print(response.content)
else:
    print("Please enter something")