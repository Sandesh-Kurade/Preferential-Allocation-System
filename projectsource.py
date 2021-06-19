#!/usr/bin/env python

import pandas as pd

import argparse

def selectTop(df, preference, subject, limit):
    top = df[df[preference] == subject]
    if limit:
        selected = top.head(limit)
    else:
        selected = top
    rejected = top.tail(len(top) - len(selected))
    print(
        f"Out of {len(top)}, {len(selected)} got selected and {len(rejected)} got rejected.")
    return selected, rejected


def subAllocation(data, pref_list, sub_list):
    for pref in preference_list:
        if len(data) == 0:
            break
        for sub in subject_list:
            print(f"\n{pref} -- {sub}")

            vacancy = limit - len(sub_dataframes[sub])

            selected, rejected = selectTop(
                df=data, preference=pref, subject=sub, limit=vacancy)
            data.drop(selected.index, axis=0, inplace=True)

            sub_dataframes[sub] = sub_dataframes[sub].append(selected)

        print("-" * 100)



parser = argparse.ArgumentParser()
parser.add_argument('location', help='records location', type=str)

args = parser.parse_args()

pathtocsv = args.location
data = pd.read_csv(pathtocsv)
data = data.sort_values(by=['CPI'], ascending=False)

preference_list = ["First Preference ", "Second Preference ",
                   "Third Preference ", "Fourth Preference "]
subject_list = ["IPR", "ML", "VT", "IOT"]


sub_dataframes = {}
for sub in subject_list:
    sub_dataframes[sub] = pd.DataFrame()


limit = 30
subAllocation(data=data, pref_list=preference_list, sub_list=subject_list)

print("BEFORE")
for sub in subject_list:
    #     print("\n", len(sub_dataframes[sub]), "\n", sub_dataframes[sub])
    print(f"For -- {sub}", len(sub_dataframes[sub]))


subject_to_remove = None
df_to_remove = None

for sub in subject_list:
    if len(sub_dataframes[sub]) < 15:
        subject_to_remove = sub
        df_to_remove = sub_dataframes[sub]


print(f"\n{subject_to_remove} does not satisfy condition, hence will be removed !")

preference_list = preference_list[1:]
subject_list.remove(subject_to_remove)

subAllocation(data=df_to_remove,  pref_list=preference_list,
              sub_list=subject_list)

print("AFTER:")
for sub in subject_list:
    #     print("\n", len(sub_dataframes[sub]), "\n", sub_dataframes[sub])
    print(f"For -- {sub}", len(sub_dataframes[sub]))


for sub, sub_df in sub_dataframes.items():
    if len(sub_df) != 0:
        sub_df.to_csv(f"{sub}_selected.csv")
