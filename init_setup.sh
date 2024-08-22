# write code to create virtual environment and installation of git

echo[$(date)]: "Start to create conda virtual environment named env"

conda create --prefix env python==3.10
echo[$(date)]: "Activate the conda virtual environment"
conda activate env

echo[$(date)]: "Adding the git"

git init
echo[$(date)]: "adding the README.md file"
#first make a file of name README.md
git add README.md

echo[$(date)]: "now commit the first commit for push first file"
git commit -m "README.md file added"
git branch -M main
git remote add origin https://github.com/ankitgaur0/weather_prediction.git
git push -u origin main