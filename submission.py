import json
import os
from tqdm import tqdm
import argparse


def parse_args():

    parser = argparse.ArgumentParser(description="Finetune a Bert-DST model")

    parser.add_argument(
        "--input_dir",
        type=str,
        default='pred_res_150000_dev_dstc8_all_',
        help="input file",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default='submission.csv',
        help="output file",
    )

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    file_names = os.listdir(args.input_dir)

    # read and store all of the data
    # print(file_names)
    ans={}
    """
    covert your datas in the following format:
     ans = {
        dialogue_id1: {service1-slot1: value1, service1-slot2: value2, ...},
        dialogue_id2: {service2-slot3: value3, service3-slot4: value4, ...},
    }
    """

    for i in tqdm(range(len(file_names))):
        with open(args.input_dir + '/' + file_names[i],'r',encoding='utf-8') as f:
            data = json.load(f)
            for j in range(len(data)):   ## number of dialogs
                dialog_dict = {}
                dialog_id = data[j]['dialogue_id']
                for k in range(len(data[j]['turns'][-2]['frames'])):
                    ## test ##
                    # print(data[j]['turns'][-2]['frames'][k]['service'])
                    # print(data[j]['turns'][-2]['frames'][k]['state']['slot_values'])
                    # print(len(data[j]['turns'][-2]['frames'][k]['state']['slot_values']))
                    ## test ##
                    service = data[j]['turns'][-2]['frames'][k]['service']
                    for key in data[j]['turns'][-2]['frames'][k]['state']['slot_values'].keys():
                        dialog_dict[service+str('-')+key] = "".join(data[j]['turns'][-2]['frames'][k]['state']['slot_values'][key])
                ans[dialog_id]=dialog_dict


    """
    prepare your answers in the following format:
    ans = {
        dialogue_id1: {service1-slot1: value1, service1-slot2: value2, ...},
        dialogue_id2: {service2-slot3: value3, service3-slot4: value4, ...},
    }
    output_path = 'submission.csv'
    """

    ans = sorted(ans.items(), key=lambda x: x[0])
    with open(args.output_dir, 'w') as f:
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
    print("finish")

if __name__ == '__main__':
    main()
