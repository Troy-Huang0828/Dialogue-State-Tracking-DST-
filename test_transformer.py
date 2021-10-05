import json
import os
from tqdm import tqdm
import argparse

def parse_args():
  parser = argparse.ArgumentParser(description="Finetune a transformers model on a text classification task")
  parser.add_argument(
    "--test_name",
    type=str,
    default='test_seen',
    help="The name of the dataset to use (via the datasets library).",
  )

  args = parser.parse_args()
  return args

args = parse_args()

dirPath = args.test_name
file_list = os.listdir(dirPath)
for name in tqdm(file_list):
  if name != 'schema.json':
    file = os.path.join( args.test_name, name)
    with open(file, 'r', encoding='utf-8') as f:
      data = json.load(f)
      final_list = []
      state = {"active_intent":[],"requested_slots":[],"slot_values": {}}

      for ind in range(len(data)):
        turn_out = []
        big_dic = {}
        turns = data[ind]["turns"]
        diol_id = data[ind]["dialogue_id"]
        services = data[ind]["services"]
        # print(services)
        big_dic["dialogue_id"] = diol_id
        big_dic["services"] = services
        turn_id = 0
        for j in range(len(turns)):
          frames = []
          speaker = turns[j]["speaker"]
          if speaker == 'USER':
            for k in services:
              dictionary = {"actions": [], "service": "", "slots": [], "state": state}
              dictionary["service"] = k
              frames.append(dictionary)
          if speaker == 'SYSTEM':
           pass
          turn_out_dict = {"frames": frames}
          utterance = turns[j]["utterance"]
          turn_out_dict["speaker"] = speaker
          turn_out_dict["turn_id"] = str(turn_id)
          turn_out_dict["utterance"] = utterance
          turn_out.append(turn_out_dict)
          turn_id+=1
        big_dic["turns"] = turn_out
        # print(big_dic)
        final_list.append(big_dic)


    output_file = os.path.join(args.test_name, name)
    with open(output_file, 'w', encoding='utf-8') as fp:
      json.dump(final_list, fp, indent=2)


