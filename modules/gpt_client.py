from .loadKeys import keys

def ask_gpt(prompt, model="gpt-3.5-turbo", max_tokens=512, temperature=0.7):
    """
    Envia prompt para OpenAI GPT-3.5-turbo e retorna a resposta gerada.
    """
    openai = keys.get_openai_client()

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            n=1,
            stop=None,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❗ GPT request failed: {e}")
        return "Sorry, I couldn't process your request."

