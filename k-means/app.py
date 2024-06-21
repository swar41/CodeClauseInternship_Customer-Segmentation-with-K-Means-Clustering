import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/customer_data.csv'
customer_data = pd.read_csv(file_path)

data = customer_data.copy()
label_encoders = {}
categorical_columns = ['gender', 'education', 'region', 'loyalty_status', 'purchase_frequency', 'product_category']

for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

numerical_columns = ['age', 'income', 'purchase_amount', 'promotion_usage', 'satisfaction_score']
scaler = StandardScaler()
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

X = data.drop(columns=['id'])
sample_data = X.sample(frac=0.1, random_state=42)
inertia_sample = []
range_clusters = range(1, 11)

for k in range_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(sample_data)
    inertia_sample.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range_clusters, inertia_sample, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Number of Clusters (Sample Data)')
plt.grid(True)
plt.show()

optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
clusters = kmeans.fit_predict(X)
customer_data['Cluster'] = clusters
customer_data.to_csv('clustered_customer_data.csv', index=False)