export OPENAI_LOGDIR="/mnt/disk1/zhangzr/Guided-Diffusion-Output/diffusion"
MODEL_FLAGS="--attention_resolutions 32,16,8 --class_cond True --diffusion_steps 1000 --image_size 256 --learn_sigma True --noise_schedule linear --num_channels 256 --num_head_channels 64 --num_res_blocks 2 --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
# TRAIN_FLAGS="--lr 1e-4 --batch_size 128 --microbatch 4"
TRAIN_FLAGS="--lr 1e-4 --batch_size 2 --lr_anneal_steps 300000"
CUDA_VISIBLE_DEVICES=0 python scripts/image_train.py --data_dir datasets/CottonWeedID15-sub10 $MODEL_FLAGS $TRAIN_FLAGS --pretrained_ckpt Guided-Diffusion-Pretrained-Ckpts/256x256_diffusion.pt