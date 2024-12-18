# PDF OCR Text Extraction

Ce script Python permet d'extraire le texte de fichiers PDF en utilisant la reconnaissance optique de caractères (OCR). Il est particulièrement utile pour les PDF contenant des images ou du texte non sélectionnable.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé les dépendances suivantes :

```bash
pip install pytesseract
pip install pdf2image
pip install Pillow
```

Vous devez également installer Tesseract OCR sur votre système :
- Windows : Téléchargez et installez depuis le [dépôt GitHub de Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux : `sudo apt-get install tesseract-ocr`
- macOS : `brew install tesseract`

## Installation

1. Clonez ce dépôt ou téléchargez le fichier `pdf-ocr-extraction.py`
2. Installez les dépendances Python requises
3. Si vous êtes sous Windows, décommentez et modifiez la ligne suivante dans le script pour pointer vers votre installation de Tesseract :
```python
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Utilisation

Le script peut être utilisé de deux manières :

1. En tant que module importé :
```python
from pdf_ocr_extraction import pdf_to_text

texte = pdf_to_text("chemin/vers/votre/fichier.pdf", language="fra")
print(texte)
```

2. En tant que script autonome :
```bash
python pdf-ocr-extraction.py
```
Dans ce cas, modifiez la variable `pdf_file` à la fin du script pour pointer vers votre fichier PDF.

## Paramètres

La fonction `pdf_to_text` accepte deux paramètres :
- `pdf_path` (str) : Chemin vers le fichier PDF à traiter
- `language` (str, optionnel) : Code de langue pour l'OCR (par défaut "fra" pour français)
  - "fra" pour français
  - "eng" pour anglais
  - Autres codes disponibles dans la documentation de Tesseract

## Sortie

Le script :
1. Convertit chaque page du PDF en image
2. Effectue l'OCR sur chaque image
3. Combine le texte extrait de toutes les pages
4. Sauvegarde automatiquement le résultat dans un fichier texte `[nom_du_pdf]_extracted.txt`
5. Retourne le texte extrait

## Gestion des erreurs

Le script inclut une gestion basique des erreurs et affichera un message si un problème survient pendant l'exécution. Les erreurs courantes peuvent inclure :
- PDF introuvable
- Problèmes de permissions
- Erreurs de conversion PDF vers image
- Erreurs d'OCR

## Limitations

- La qualité de l'extraction dépend de la qualité du document source
- Les PDF complexes (colonnes multiples, mise en page élaborée) peuvent ne pas être parfaitement traités
- Le temps de traitement augmente avec le nombre de pages
