avconv -i MAH00249.mp4 -vcodec libx264 -acodec aac -bsf:v h264_mp4toannexb -f mpegts -strict experimental -vf "movie=out.png[watermark];[in][watermark] overlay=10:10[out] " -y 1.ts