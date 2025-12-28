#!/bin/bash

echo "🚀 배포를 시작합니다..."

PID=$(pgrep -f "python3 app.py")

if [ -z "$PID" ]; then
	echo "✅ 기존에 실행 중인 서버가 없습니다."
else
	echo"💀 기존 서버(PID: $PID)를 종료합니다..."
	kill -9 $PID
fi

echo "📥 Git Pull 수행 중..."
git pull origin master

echo "🔥 서버를 다시 시작합니다..."

nohup python3 app.py > output.log 2>&1 &

echo "🎉 배포 완료! (잠시 후 접속해보세요)"

