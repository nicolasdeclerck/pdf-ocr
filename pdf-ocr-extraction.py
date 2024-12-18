import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os


def pdf_to_text(pdf_path, language="fra"):
    """
    Extrait le texte d'un PDF en utilisant OCR.

    Args:
        pdf_path (str): Chemin vers le fichier PDF
        language (str): Code de langue pour Tesseract (fra pour français, eng pour anglais)

    Returns:
        str: Texte extrait du PDF
    """

    # Sur Windows, spécifiez le chemin vers Tesseract si nécessaire
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    try:
        # Convertir le PDF en images
        print("Conversion du PDF en images...")
        pages = convert_from_path(pdf_path)

        # Extraire le texte de chaque page
        text_content = []
        for i, page in enumerate(pages, start=1):
            print(f"Traitement de la page {i}/{len(pages)}...")
            text = pytesseract.image_to_string(page, lang=language)
            text_content.append(text)

        # Combiner le texte de toutes les pages
        final_text = "\n\n".join(text_content)

        # Optionnel : sauvegarder le résultat dans un fichier texte
        output_file = os.path.splitext(pdf_path)[0] + "_extracted.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_text)

        print(f"Extraction terminée. Résultat sauvegardé dans : {output_file}")
        return final_text

    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")
        return None


# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez par le chemin de votre PDF
    pdf_file = "cadrage.pdf"
    extracted_text = pdf_to_text(pdf_file)
