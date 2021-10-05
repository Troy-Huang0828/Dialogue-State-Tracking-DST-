# Applied Deep Learning final (DST/NLG)
## step 1: environment setup
* pip install -r requirements.txt 
* tensorflow_GPU version 

thus you need to use two commands below:
```shell
pip install -r requirements.txt
conda install tensorflow-gpu=1.14.0
```
If you don't have anaconda or install failed , you will ues pip to install tensorflow ,cudnn and cudatoolkit.

```shell
pip install tensorflow_gpu == 1.14.0
pip install cudnn 
pip install cudatoolkit
````
## step 2: data download
####We use wget command to download the data on dropbox. 
If you don't have wget, plz download the wget with this address:
https://eternallybored.org/misc/wget/
```shell
bash download.sh
```
After you download the model, you should transform test data into the specify format 

(train/dev/test data we all put into data file)
```shell
bash trans.py ${1} ${2}
${1}:The path to seen data or unseen data
${2}:type seen or unseen
example: bash trans.sh path/test_seen seen
```
##step 3: train / prediction with Bert-dst
Explain the names in flags:
 
bert_ckpt_dir --> (directory of initial pretrain bert model)

task_name --> ["dstc8_single_domain","dstc8_multi_domain","dstc8_all"]

dstc8_data_dir --> (directory of SGD includes train / dev / test)

run_mode --> ["train", "predict"]

schema_embedding_dir --> (after date prepocessing the directory of schema embedding will be put)

dialogues_example_dir --> (after date prepocessing the directory of dialogues embedding will be put)

dataset_split --> ["train","dev","test_seen","test_unseen"] the data which you want to train / predict

eval_ckpt --> (type:int) The checkpoint step you want to use on prediction.  
```shell
fine-tune model on train data:
python train.py
predict on test_seen data:
python predict_seen.py
predict on test_unseen data:
python predict_unseen.py
```

##step 4: state to csv  
"${1}": path to the prediction data file.

"${2}": path to the output submission csv file.

ex : bash ./state_to_csv.sh ./output_ft/pred_res_1050000_test_seen_dstc8_all_ ./predict_1050000.csv

```shell
bash ./state_to_csv.sh "${1}" "${2}"
```
##step 5 : Dev score ( joint accuracy )
"${1}": path to the dev ground true csv file.

"${2}": path to the predict file.

ex : bash ./score.sh ./ground_ture.csv  ./pred_res_150000_dev_dstc8_all_
```shell
bash ./score.sh "${1}" "${2}"

```
