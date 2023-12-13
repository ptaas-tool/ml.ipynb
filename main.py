# Import the necessary libraries
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Prepare your data
# Assuming you have your feature data in X and label data in y

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create an instance of the SVM classifier
clf = SVC(kernel='linear')

# Step 4: Train the SVM classifier
clf.fit(X_train, y_train)

# Step 5: Make predictions with the trained model
predictions = clf.predict(X_test)

# Step 6: Evaluate the performance of the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
