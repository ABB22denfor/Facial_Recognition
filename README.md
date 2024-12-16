# Face Recognition Project

## Beskrivning
Detta projekt implementerar ansiktsigenkänning i realtid med hjälp av OpenCV och DeepFace-biblioteket. Systemet kan känna igen en person från en uppsättning referensbilder och visa deras namn på videoströmmen om en matchning hittas.

## Funktioner
- **Kameraingång:** Använder antingen datorns inbyggda kamera eller en extern kamera.
- **Ansiktsigenkänning:** Jämför ansikten i realtid med förinlästa referensbilder.
- **Trådhantering:** Använder trådar för att förbättra prestanda och förhindra att huvudprogrammet blockeras.
- **Visuell återkoppling:** Visar identifierad persons namn eller "NOT FOUND" på videoströmmen.

## Förutsättningar

Se till att följande program och bibliotek är installerade:

- Python 3.6 eller senare
- OpenCV
- DeepFace
- NumPy
- tf-keras

## Installation
1. Klona detta repository:
   ```
   git clone <repository-url>
   ```

2. Installera nödvändiga Python-paket:
   ```
   pip install opencv-python deepface numpy tf-keras
   ```

3. Skapa en mapp som heter `images/` och lägg till undermappar med personnamn som namn. Lägg till referensbilder för varje person i respektive undermapp. Exempel:
   ```
   images/
   ├── Jocke/
   │   ├── jocke.jpg
   ├── Sofie/
       ├── sofie.jpg
   ```

## Hur man använder
1. Starta programmet genom att köra huvudskriptet:
   ```
   python main.py
   ```

2. Videoströmmen visas i ett nytt fönster. Tryck på **q** för att avsluta.

## Struktur
- **`main.py`**: Huvudskriptet som hanterar kamerainspelning och ansiktsigenkänning.
- **`images/`**: Mappen som innehåller referensbilder.

## Licens
Detta projekt är licensierat under [MIT-licensen](LICENSE).

## Förbättringsområden
- Anpassa koden så att flertal bilder kan användas för att analysera om personen på videon matchar en av bilderna
