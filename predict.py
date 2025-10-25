import openai
import os

# Stelle sicher, dass dein OpenAI API Key als Umgebungsvariable gesetzt ist
# (auf Replicate oder lokal): OPENAI_API_KEY

def generate_description(product_link=None, product_image=None, tone="du", style="werbung", length=400):
    """
    Generates a unique, SEO-optimized product description using GPT-5.
    The model can analyze a product link and optionally an image.
    """

    base_prompt = f"""
    Schreibe eine professionelle, kreative und werbewirksame Produktbeschreibung 
    mit etwa {length} Wörtern. Sie basiert auf dem Produkt unter diesem Link: {product_link or "kein Link"}.
    Falls ein Bild angegeben wurde ({'vorhanden' if product_image else 'nicht vorhanden'}), berücksichtige es ebenfalls.

    Verwende einen flüssigen, emotionalen Schreibstil in {tone}-Ansprache (Du/Sie je nach Wahl), 
    mit einem lebendigen und authentischen Ton ({style}). 
    Schreibe vollständig unique, ohne Textteile zu kopieren. 
    Der Text darf nicht von KI-Detektoren als KI erkannt werden.
    """

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Du bist ein professioneller deutscher Werbetexter."},
            {"role": "user", "content": base_prompt}
        ],
        temperature=0.9,
    )

    return response.choices[0].message.content.strip()
