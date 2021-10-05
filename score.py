import json
import os
from tqdm import tqdm
import pandas as pd
import argparse




def collect_data(folder_path):
    file_names = os.listdir(folder_path)
    # read and store all of the data
    print(file_names)
    ans = {}
    for i in tqdm(range(len(file_names))):
        with open(folder_path + '/' + file_names[i], 'r', encoding='utf-8') as f:
            data = json.load(f)
            for j in range(len(data)):  ## number of dialogs
                dialog_list = []
                dialog_dict = {}
                dialog_id = data[j]['dialogue_id']
                for k in range(len(data[j]['turns'][-2]['frames'])):
                    # print(data[j]['turns'][-2]['frames'][k]['service'])
                    # print(data[j]['turns'][-2]['frames'][k]['state']['slot_values'])
                    service = data[j]['turns'][-2]['frames'][k]['service']
                    for key in data[j]['turns'][-2]['frames'][k]['state']['slot_values'].keys():
                        dialog_dict[service + str('-') + key] = "".join(
                            data[j]['turns'][-2]['frames'][k]['state']['slot_values'][key])
                ans[dialog_id] = dialog_dict
    return ans

def state_to_csv(ans,output_path):
    ans = sorted(ans.items(), key=lambda x: x[0])
    with open(output_path, 'w') as f:
        f.write('id,state\n')
        for dialogue_id, states in ans:
            if len(states) == 0:  # no state ?
                str_state = 'None'
            else:
                states = sorted(states.items(), key=lambda x: x[0])
                str_state = ''
                for slot, value in states:
                    # NOTE: slot = "{}-{}".format(service_name, slot_name)
                    str_state += "{}={}|".format(
                        slot.lower(), value.replace(',', '_').lower())
                str_state = str_state[:-1]
            f.write('{},{}\n'.format(dialogue_id, str_state))
    print("save to csv")

def score(ground_true_path,predict_path):
    ground_true_data = pd.read_csv(ground_true_path)
    predict_path = pd.read_csv(predict_path)
    count = 0
    for i in range(len(ground_true_data)):
        if ground_true_data['id'][i] == predict_path['id'][i]:
            if ground_true_data['state'][i] == predict_path['state'][i]:
                # print("gt:",ground_true_data['state'][i])
                # print("pd",predict_path['state'][i])
                count += 1
            else:
                pass
        else:
            print("id error!!!!")
    print("accuracy:",count/len(ground_true_data) * 100)

def parse_args():

    parser = argparse.ArgumentParser(description="Finetune a Bert-DST model")

    parser.add_argument(
        "--ground_true_dir",
        type=str,
        default='D:/ADL/final/ground_ture.csv',
        help="input file",
    )
    parser.add_argument(
        "--predict_fold",
        type=str,
        default='C:/Users/LAB228/Desktop/pred_res_150000_dev_dstc8_all_',
        help="output file",
    )
    args = parser.parse_args()

    # if args.output_model_dir is not None:
    #     os.makedirs(args.output_model_dir, exist_ok=True)
    return args




def main():
    args = parse_args()

    ## predict data ##
    answer_predict= collect_data(args.predict_fold)
    state_to_csv(answer_predict,'./predict.csv')
    score(args.ground_true_dir,'./predict.csv')


if __name__ == '__main__' :
    main()
