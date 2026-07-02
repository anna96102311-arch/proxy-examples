import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():
    load_dotenv()

    model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
)

    response = model.invoke("Say hello from Rapidproxy through LangChain.")

    print(response.content)


if __name__ == "__main__":
    main()