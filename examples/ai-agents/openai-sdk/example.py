import os

from dotenv import load_dotenv
from openai import DefaultHttpxClient, OpenAI


def main():
    load_dotenv()

    proxy_url = (
        f"http://{os.getenv('RAPIDPROXY_USERNAME')}:"
        f"{os.getenv('RAPIDPROXY_PASSWORD')}@"
        f"{os.getenv('RAPIDPROXY_HOST')}:"
        f"{os.getenv('RAPIDPROXY_PORT')}"
    )

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        http_client=DefaultHttpxClient(proxy=proxy_url),
    )

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        input="Say hello from Rapidproxy.",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()