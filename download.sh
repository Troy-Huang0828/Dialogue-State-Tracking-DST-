mkdir cased_L-12_H-768_A-12
cd cased_L-12_H-768_A-12
wget https://www.dropbox.com/s/oxd6nrsutqefkrs/bert_config.json?dl=1 -O bert_config.json
wget https://www.dropbox.com/s/kwmq5hs8wz2u724/bert_model.ckpt.data-00000-of-00001?dl=1 -O bert_model.ckpt.data-00000-of-00001
wget https://www.dropbox.com/s/mt0wrwt793eko97/bert_model.ckpt.index?dl=1 -O bert_model.ckpt.index
wget https://www.dropbox.com/s/ox4ogyfhcl7lrzn/bert_model.ckpt.meta?dl=1 -O bert_model.ckpt.meta
wget https://www.dropbox.com/s/luf9my4blqk261x/vocab.txt?dl=1 -O vocab.txt
cd ..
mkdir ground_truth
cd ground_truth
wget https://www.dropbox.com/s/4isf3ykdo5peqfk/dev_ground_ture.csv?dl=1 -O dev_ground_ture.csv
cd ..
mkdir output_dialogues_example
mkdir output_ft
mkdir output_schema_embedding
cd output_ft
wget https://www.dropbox.com/s/m7jcmjwn2xwzrt9/model.ckpt-1050000.index?dl=1 -O model.ckpt-1050000.index
wget https://www.dropbox.com/s/2p1bzb11rhsyc9p/model.ckpt-1050000.meta?dl=1 -O model.ckpt-1050000.meta
wget https://www.dropbox.com/s/lf2anicyuxjbpkh/model.ckpt-1050000.data-00000-of-00001?dl=1 -O model.ckpt-1050000.data-00000-of-00001

