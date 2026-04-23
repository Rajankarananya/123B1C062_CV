# Intelligent Number Plate Recognition System (INPRS)

A computer vision project for number plate detection, OCR-based text extraction, state identification, vehicle logging, and dashboard visualization.

This repository also contains multiple experimental scripts for localization, augmentation, segmentation, feature extraction, sequence modeling, and data preparation.

## Features

- Number plate localization using contour-based filtering
- OCR extraction with EasyOCR
- State detection from plate/state code mapping
- Vehicle entry logging to CSV
- Duplicate detection and simple stolen-vehicle alert checks
- Parking analytics (occupied/available/unique counts)
- Streamlit dashboard for interactive uploads
- Utility scripts for:
  - dataset split
  - basic augmentation
  - corner detection
  - region growing
  - perspective correction
  - CNN feature extraction
  - Transformer sequence model prototype

## Project Structure

- `app.py`: Streamlit dashboard for image upload, plate reading, logs, and analytics
- `main.py`: End-to-end offline pipeline (load image -> detect plate -> OCR -> log -> analytics)
- `check.py`: Counts state-wise image files in dataset folders
- `split_dataset.py`: Splits dataset images into train/val/test (70/15/15)
- `augment.py`: Saves rotated, blurred, and brightness-adjusted sample outputs
- `hybrid_localization.py`: Contour + corner based plate localization visualization
- `advanced_corners.py`: Corner detection demo (`goodFeaturesToTrack`)
- `region_growing.py`: Flood-fill based region growing demo
- `perspective_fix.py`: Perspective transform correction demo
- `cnn_features.py`: ResNet18 forward pass on cropped plate image
- `transformer_decoder.py`: PyTorch Transformer prototype for sequence modeling
- `metrics.py`: Prints placeholder training metrics
- `utils.py`: Empty placeholder module
- `vehicle_log.csv`: Vehicle entry log file
- `dataset/`: Source dataset (state-wise folders)
- `dataset_split/`: Train/validation/test split output
- `outputs/`: Generated intermediate/final output images

## Requirements

Current `requirements.txt` includes:

- opencv-python
- easyocr
- imutils
- streamlit

Some scripts also require additional packages that are not listed in `requirements.txt`:

- torch
- torchvision
- pandas
- pillow
- numpy

Install all required dependencies:

```bash
pip install -r requirements.txt
pip install torch torchvision pandas pillow numpy
```

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Ensure dataset images are available under `dataset/State-wise_OLX/...`.

Example (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install torch torchvision pandas pillow numpy
```

## How To Run

### 1) Main pipeline (offline)

```bash
python main.py
```

What it does:

- Loads sample image from `dataset/State-wise_OLX/DL/DL1.jpg`
- Detects candidate plate region
- Performs OCR on cropped plate (fallback OCR on full image)
- Saves outputs to `outputs/`
- Appends vehicle data to `vehicle_log.csv`
- Prints stolen/duplicate/parking statistics

### 2) Streamlit dashboard

```bash
streamlit run app.py
```

Dashboard includes:

- Upload vehicle image
- Plate + state detection
- CSV log updates
- Parking metrics cards
- Table view of all logs

### 3) Dataset tools

- Split dataset:

```bash
python split_dataset.py
```

- Check class/state image counts:

```bash
python check.py
```

### 4) Experimental modules

```bash
python augment.py
python hybrid_localization.py
python advanced_corners.py
python region_growing.py
python perspective_fix.py
python cnn_features.py
python transformer_decoder.py
python metrics.py
```

## Inputs and Outputs

### Inputs

- Vehicle images (`.jpg/.jpeg/.png`) in dataset folders or uploaded via Streamlit

### Outputs

- Image artifacts in `outputs/` (for example `detected_plate.jpg`, `cropped_plate.jpg`)
- CSV logs in `vehicle_log.csv`
- Console metrics/status prints

## Notes

- `main.py` and several demos use hard-coded paths (for example `dataset/State-wise_OLX/DL/DL1.jpg`).
- State dictionary in `main.py`/`app.py` currently includes a subset of Indian state codes.
- Stolen-vehicle list in `main.py` is a static demo list.
- `metrics.py` currently prints fixed values (not loaded from training logs).

## Suggested Improvements

- Add CLI arguments for input image path and output directory
- Move constants (state map, stolen list, slot count) to config file
- Add robust plate text post-processing and regex validation
- Expand state code mapping to full set
- Add unit tests and integration tests
- Include model training/evaluation scripts and real metric logging
- Add proper `requirements.txt` coverage for all scripts

## License

No license file is currently included. Add a license if this repository will be distributed publicly.
