tmux kill-server
cd mlh-fellowship/
git fetch && git reset origin/main --hard
export FLASK_ENV=development
tmux new -d 'flask run --host=0.0.0.0'
