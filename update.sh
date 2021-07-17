clear
echo "Installing Update & Requirements"
echo ""
apt update && apt upgrade -y
apt install rename ffmpeg python3-pip -y
pip install pytube
