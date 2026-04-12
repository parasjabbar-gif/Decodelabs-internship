# Project 2 - Data Classification Using AI
# Using KNN Algorithm

# STEP 1: Import libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# STEP 2: Load dataset
iris = datasets.load_iris()

X = iris.data      # Features
y = iris.target    # Target

print("Dataset Loaded Successfully")

# STEP 3: Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Data Split Done")

# STEP 4: Apply KNN algorithm
model = KNeighborsClassifier(n_neighbors=5)

# STEP 5: Train model
model.fit(X_train, y_train)

print("Model Training Completed")

# STEP 6: Make predictions
y_pred = model.predict(X_test)

# STEP 7: Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Prediction Completed")
print("Accuracy of Model:", accuracy)