# End-of-Life (EOL) Data Fetcher

## 📌 Overview

This Python script fetches end-of-life (EOL) data for various software products from the [End of Life API](https://endoflife.date). It retrieves information about the product's release cycle, EOL date, and latest version, then saves it into a CSV file. Each time the script runs, it overwrites the existing CSV file with the latest data.

## 🚀 Features

- Automatically retrieves a list of all available products from the API.
- Fetches detailed EOL information for each product.
- Saves the data into a structured `eol_data.csv` file.
- Overwrites the file on each run to ensure the data is always up to date.
- Handles request errors gracefully with informative messages.

## 📂 Output Format

The script generates a CSV file (`eol_data.csv`) with the following columns:

- **product**: Name of the software product.
- **cycle**: Version cycle of the product.
- **eol**: End-of-life date.
- **latest**: Latest available version.

## 🛠 Installation

### Prerequisites

Ensure you have **Python 3.x** installed. You can check with:

```sh
python3 --version
```

You also need to install the requests module if it's not already installed:

```sh
pip install requests
```


### Clone the Repository

```sh
git clone https://github.com/marusjapl/EOL.git
cd EOL
```

## ▶️ Usage

Run the script in your terminal:

```sh
python eol.py
```

For Python 3:

```sh
python3 eol.py
```

## 📊 Viewing the Data

Once executed, the `eol_data.csv` file will be generated in the same directory. Since the file is overwritten with each execution, it always contains the most up-to-date information. You can open it using:

```sh
cat eol_data.csv  # View in terminal
```
