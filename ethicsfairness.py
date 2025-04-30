# Ethics in AI, Fairness in AI, Legal perspective

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# --- Sample Dataset (Simulating Bias in AI) ---
# Gender bias in loan approval prediction
data = {
    'income': [50000, 60000, 35000, 45000, 80000, 70000],
    'gender': ['male', 'female', 'female', 'male', 'male', 'female'],
    'approved': [1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# --- Encode Categorical Data ---
le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])  # male=1, female=0

# --- Fairness Check (Before Training) ---
def fairness_analysis(df):
    print("\n--- Fairness Analysis ---")
    group_means = df.groupby('gender')['approved'].mean()
    print("Approval Rates by Gender:\n", group_means)
    disparity = abs(group_means['male'] - group_means['female'])
    print("Disparity in Approval Rate:", disparity)
    if disparity > 0.2:
        print("⚠️ Potential Bias Detected!")
    else:
        print("✅ Fairness Seems Acceptable.")

# --- Legal Compliance Simulation ---
def check_user_consent(user_agreed):
    print("\n--- Legal Compliance (Consent Check) ---")
    if user_agreed:
        print("✅ User consent provided. Data use permitted.")
    else:
        raise PermissionError("❌ Consent required under data protection laws (e.g., GDPR).")

# --- Ethical Model Evaluation ---
def ethical_decision_score(y_true, y_pred):
    print("\n--- Ethical Evaluation ---")
    acc = accuracy_score(y_true, y_pred)
    fairness_penalty = abs(sum(y_pred[:3]) - sum(y_pred[3:])) / len(y_pred)
    ethical_score = acc - fairness_penalty
    print(f"Accuracy: {acc:.2f}, Fairness Penalty: {fairness_penalty:.2f}")
    print(f"Ethical Score: {ethical_score:.2f}")
    return ethical_score

# --- ML Model Training and Evaluation ---
def run_model(df):
    X = df[['income', 'gender_encoded']]
    y = df['approved']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    ethical_decision_score(y_test, y_pred)

# --- Main Program ---
def main():
    fairness_analysis(df)

    try:
        # Simulate legal scenario
        user_consent = True  # Change to False to simulate denial
        check_user_consent(user_consent)
    except PermissionError as e:
        print(e)
        return

    # Run model and assess fairness
    run_model(df)

if __name__ == "__main__":
    main()
