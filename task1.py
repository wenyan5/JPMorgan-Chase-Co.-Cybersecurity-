import pandas as pd
import matplotlib.pyplot as plt

file = "transactions.csv"


def exercise_0(file):
    return pd.read_csv(file)


def exercise_1(df):
    # column_names = df.columns.tolist()
    # return column_names
    return list(df)

def exercise_2(df, k):
    first_k_rows = df.head(k)
    return first_k_rows


def exercise_3(df, k):
    random_sample = df.sample(k)
    return random_sample


def exercise_4(df):
    # unique_types = df["type"].unique().tolist()
    # return unique_types
    return df['type'].unique()


def exercise_5(df):
    top_10_destinations = df['nameDest'].value_counts().head(10)
    return top_10_destinations


def exercise_6(df):
    fraud_rows = df[df['isFraud'] == 1]
    return fraud_rows


def exercise_7(df):
    df1 = df.groupby('nameOrig')['nameDest'].agg(['nunique'])
    #print(df1)
    df1.sort_values(by=('nunique'), ascending=False, inplace=True)
    return df1


def visual_1(df):
    def transaction_counts(df):
        # TODO
        transaction_counts = df['type'].value_counts()
        #print("transaction_counts",transaction_counts)
        return transaction_counts

    def transaction_counts_split_by_fraud(df):
        # TODO
        fraud_transaction_counts = df[df['isFraud'] == 1]['type'].value_counts()
        #print("transaction_counts_split_by_fraud",fraud_transaction_counts)
        return fraud_transaction_counts

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs[:2]:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    #plt.figure(figsize=(8, 6))
    plt.show()
    return "gg"


def visual_2(df):
    def query(df):
        # TODO
        df['Origin Delta'] = df['oldbalanceOrg'] - df['newbalanceOrig']
        df['Destination Delta'] = df['oldbalanceDest'] - df['newbalanceDest']
        return df[df['type'] == 'CASH_OUT']

    plot = query(df).plot.scatter(x='Origin Delta',y='Destination Delta')
    plot.set_title('Source v. Destination Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    plt.show()
    return


def exercise_custom(df):
    return df[['isFlaggedFraud', 'isFraud']].value_counts()


def visual_custom(df):
    fig, ax = plt.subplots(1, figsize=(4, 6))
    exercise_custom(df).plot(ax=ax, kind='bar')
    ax.set_title('Fraud Detection')
    ax.set_xlabel('isFlaggedFraud, isFraud')
    ax.set_ylabel('Occurrence')
    for p in ax.patches:
        ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    plt.show()
    return "Here we see that the fraud detection at play misses almost all " \
           "of the fradulent activity. However, there are no false negatives " \
           "either. One interpretation could be that the detector does not " \
           "report until it has a high degree of confidence."



df = exercise_0('transactions.csv')
column_names = exercise_1(df)
first_k_rows = exercise_2(df, 5)
random_sample = exercise_3(df, 5)
unique_types = exercise_4(df)
top_10_destinations = exercise_5(df)
fraud_rows = exercise_6(df)
# print(fraud_rows)
exercise_7(df)
#visual_1(df)
#visual_2(df)
visual_custom(df)