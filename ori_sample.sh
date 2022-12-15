export OPENAI_LOGDIR="./Guided-Diffusion-Output/sample-no-guided-step1000"
# SAMPLE_FLAGS="--batch_size 2  --num_samples 4685 --timestep_respacing 250"
SAMPLE_FLAGS="--batch_size 4  --num_samples 100"
MODEL_FLAGS="--attention_resolutions 32,16,8 --class_cond True --diffusion_steps 1000 --image_size 256 --learn_sigma True --noise_schedule linear --num_channels 256 --num_head_channels 64 --num_res_blocks 2 --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
python ./scripts/image_sample.py $MODEL_FLAGS --model_path ./Guided-Diffusion-Output/diffusion/ema_0.9999_300000.pt $SAMPLE_FLAGS