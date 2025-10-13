@echo off
echo 🚀 Starting CI/CD Deployment...

echo ✅ Running tests...
python manage.py test
if errorlevel 1 (
    echo ❌ Tests failed!
    exit /b 1
)

echo 📁 Copying files to server...
scp -r -i ~/.ssh/id_ed25519 .\* kelemnik@192.168.0.107:/home/kelemnik/app/

echo 🔧 Running deployment commands...
ssh -i ~/.ssh/id_ed25519 kelemnik@192.168.0.107 "
  cd /home/kelemnik/app
  python3 -m pip install -r requirements.txt
  python3 manage.py migrate
  python3 manage.py collectstatic --noinput
  echo 🎉 DEPLOYMENT COMPLETED!
"

echo ✅ CI/CD Pipeline finished successfully!
pause