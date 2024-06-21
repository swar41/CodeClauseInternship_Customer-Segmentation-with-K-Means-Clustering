# Customer Segmentation with K-Means Clustering

This project applies K-Means clustering to segment customers based on their purchase behavior. The clustering helps identify distinct customer segments, which can be useful for targeted marketing and personalized recommendations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)


## Features

- Preprocesses customer data, including encoding categorical variables and scaling numerical variables.
- Applies the Elbow Method to determine the optimal number of clusters.
- Uses K-Means clustering to segment customers.
- Saves the segmented customer data to a CSV file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/swar41/customer-segmentation.git
    cd customer-segmentation
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install pandas scikit-learn matplotlib
    ```

4. Ensure the dataset file (`customer_data.csv`) is in the root directory of the project.

## Usage

1. Run the script:

    ```bash
    python segment_customers.py
    ```

2. The script will preprocess the data, apply the K-Means clustering algorithm, and save the clustered data to `clustered_customer_data.csv`.

## Dataset

The script expects a CSV file named `customer_data.csv` with the following columns:

- `id`: Unique identifier for each customer
- `gender`: Gender of the customer
- `age`: Age of the customer
- `income`: Income of the customer
- `education`: Education level of the customer
- `region`: Region where the customer resides
- `loyalty_status`: Loyalty status of the customer
- `purchase_frequency`: Frequency of purchases made by the customer
- `product_category`: Product category preferred by the customer
- `purchase_amount`: Amount spent by the customer on purchases
- `promotion_usage`: Usage of promotional offers by the customer
- `satisfaction_score`: Satisfaction score of the customer

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

